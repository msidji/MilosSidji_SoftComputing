using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


using Emgu.CV;                  //
using Emgu.CV.CvEnum;           // usual Emgu Cv imports
using Emgu.CV.Structure;        //
using Emgu.CV.UI;               //

namespace RA184_2012_SC
{
    public partial class formMainFrame : Form
    {
        public formMainFrame()
        {
            InitializeComponent();
        }

        private void labelTema_Click(object sender, EventArgs e)
        {

        }

        private void buttonOpenFile_Click(object sender, EventArgs e)
        {
            DialogResult drChosenFile;

            drChosenFile = ofdOpenFile.ShowDialog();

            if (drChosenFile != DialogResult.OK || ofdOpenFile.FileName == "")
            {
                lblChosenFile.Text = "file not chosen";
                return;
            }

            Mat imgOriginal;

            try
            {
                imgOriginal = new Mat(ofdOpenFile.FileName, LoadImageType.Color);
            }
            catch (Exception ex)
            {
                lblChosenFile.Text = "unable to open image, error: " + ex.Message;
                return;
            }

            if (imgOriginal == null)
            {
                lblChosenFile.Text = "unable to open image";
                return;
            }

            Mat imgGrayscale = new Mat(imgOriginal.Size, DepthType.Cv8U, 1);
            Mat imgBlurred = new Mat(imgOriginal.Size, DepthType.Cv8U, 1);
            Mat imgCanny = new Mat(imgOriginal.Size, DepthType.Cv8U, 1);

            CvInvoke.CvtColor(imgOriginal, imgGrayscale, ColorConversion.Bgr2Gray);

            CvInvoke.GaussianBlur(imgGrayscale, imgBlurred, new Size(5, 5), 1.5);

            CvInvoke.Canny(imgBlurred, imgCanny, 100, 200);

            ibOriginal.Image = imgOriginal;
            ibGrayscale.Image = imgGrayscale;
            ibThreshold.Image = imgBlurred;
            ibRegioni.Image = imgCanny;
        }

    }
}
