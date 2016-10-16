using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace streamIT_Tests
{
    class Program
    {
        static void Main(string[] args)
        {
            WebClient wb = new WebClient();
            NameValueCollection data = new NameValueCollection();
            string b64s = "";
            data["cam"] = "android";
            data["b64"] = b64s;
            var response = wb.UploadValues("http://127.0.0.1:8888/cin", "POST", data);
            Console.WriteLine(response);
            Console.ReadLine();
        }
    }
}
