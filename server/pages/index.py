from handlers import basic

class Handler(basic.Handler):
    def getgen(self, arguments):
        self.cr()
        camera = arguments["cam"][0].decode()
        doc, tag, text = self.yat
        with tag("html"):
            with tag("body"):
                text("Hello world!")
                with tag("iframe", ("src","cameras?cam=" + camera), ("id", "cam"), ("style", "visibility:noe; border: 0; width: 100%; height: 100%"), ("onload","this.style.visibility = 'block';")):
                    doc.asis("")
                with tag("script"):
                    doc.asis("""
                    setInterval (function() {
                        var iframe = document.getElementById('cam');
                        iframe.src = iframe.src;
                    }, 100);
                    """)
        return doc.getvalue()