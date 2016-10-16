using System;

using Android.App;
using Android.OS;
using Android.Views;
using Android.Widget;

using System.Net;
using System.Collections.Specialized;

namespace TextureViewCameraStream
{
    [Activity (Label = "TextureViewCameraStream", MainLauncher = true)]
    public class Activity1 : Activity, TextureView.ISurfaceTextureListener, Android.Hardware.Camera.IPictureCallback
    {
        Android.Hardware.Camera _camera;
        TextureView _textureView;
        WebClient wb = new WebClient();
        NameValueCollection data = new NameValueCollection();

        public void OnPictureTaken(byte[] arg0, Android.Hardware.Camera agr1)
        {
            Toast.MakeText(this, "Took picture", ToastLength.Short).Show();
            //string b64s = Convert.ToBase64String(arg0);
            string b64s = "";
            data["cam"] = "android";
            data["b64"] = b64s;
            var response = wb.UploadValues("http://10.33.79.13:8888/cin", "POST", data);
            Toast.MakeText(this, response.ToString(), ToastLength.Long);
        }

        protected override void OnCreate (Bundle bundle)
        {
            base.OnCreate (bundle);
   
            _textureView = new TextureView (this);
            _textureView.SurfaceTextureListener = this;
            
            SetContentView (_textureView);
        }
                
        public void OnSurfaceTextureAvailable (Android.Graphics.SurfaceTexture surface, int w, int h)
        {
            _camera = Android.Hardware.Camera.Open ();
            _textureView.LayoutParameters = new FrameLayout.LayoutParams (w, h);
            _camera.SetPreviewTexture (surface);
            _camera.StartPreview ();
            try
            {
                Toast.MakeText(this, "About to take picture", ToastLength.Short).Show();
                _camera.TakePicture(null, null, this);
                Toast.MakeText(this, "Finished pic", ToastLength.Short).Show();
                _camera = Android.Hardware.Camera.Open();
                _textureView.LayoutParameters = new FrameLayout.LayoutParams(w, h);
                _camera.SetPreviewTexture(surface);
                _camera.StartPreview();
                Toast.MakeText(this, "This shit again!", ToastLength.Short).Show();
            }
            catch (Exception e)
            {
                Toast.MakeText(this, e.ToString(), ToastLength.Long).Show();
            }
        }

        public bool OnSurfaceTextureDestroyed (Android.Graphics.SurfaceTexture surface)
        {
            Toast.MakeText(this, "About to break texture", ToastLength.Short).Show();
            _camera.StopPreview ();
            _camera.Release ();
            
            return true;
        }

        public void OnSurfaceTextureSizeChanged (Android.Graphics.SurfaceTexture surface, int width, int height)
        {
            // camera takes care of this
        }

        public void OnSurfaceTextureUpdated (Android.Graphics.SurfaceTexture surface)
        {
            
        }
      
    }
}


