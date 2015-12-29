namespace RA184_2012_SC
{
    partial class formMainFrame
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.buttonOpenFile = new System.Windows.Forms.Button();
            this.labelTema = new System.Windows.Forms.Label();
            this.tlplOuter = new System.Windows.Forms.TableLayoutPanel();
            this.tlpInner = new System.Windows.Forms.TableLayoutPanel();
            this.lblChosenFile = new System.Windows.Forms.Label();
            this.buttonGrayscale = new System.Windows.Forms.Button();
            this.ibOriginal = new Emgu.CV.UI.ImageBox();
            this.ibGrayscale = new Emgu.CV.UI.ImageBox();
            this.lblOriginalImg = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.lblThreshold = new System.Windows.Forms.Label();
            this.lblRegioni = new System.Windows.Forms.Label();
            this.ibThreshold = new Emgu.CV.UI.ImageBox();
            this.ibRegioni = new Emgu.CV.UI.ImageBox();
            this.ofdOpenFile = new System.Windows.Forms.OpenFileDialog();
            this.tlplOuter.SuspendLayout();
            this.tlpInner.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.ibOriginal)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.ibGrayscale)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.ibThreshold)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.ibRegioni)).BeginInit();
            this.SuspendLayout();
            // 
            // buttonOpenFile
            // 
            this.buttonOpenFile.AutoSize = true;
            this.buttonOpenFile.Location = new System.Drawing.Point(3, 3);
            this.buttonOpenFile.Name = "buttonOpenFile";
            this.buttonOpenFile.Size = new System.Drawing.Size(75, 23);
            this.buttonOpenFile.TabIndex = 0;
            this.buttonOpenFile.Text = "Otvori sliku";
            this.buttonOpenFile.UseVisualStyleBackColor = true;
            this.buttonOpenFile.Click += new System.EventHandler(this.buttonOpenFile_Click);
            // 
            // labelTema
            // 
            this.labelTema.AutoSize = true;
            this.tlplOuter.SetColumnSpan(this.labelTema, 2);
            this.labelTema.Dock = System.Windows.Forms.DockStyle.Fill;
            this.labelTema.Location = new System.Drawing.Point(3, 0);
            this.labelTema.Name = "labelTema";
            this.labelTema.Size = new System.Drawing.Size(985, 13);
            this.labelTema.TabIndex = 1;
            this.labelTema.Text = "Tema: Detekcija ivica puta u saobraćaju, prepoznavanje saobraćajnih znakova";
            this.labelTema.Click += new System.EventHandler(this.labelTema_Click);
            // 
            // tlplOuter
            // 
            this.tlplOuter.ColumnCount = 2;
            this.tlplOuter.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlplOuter.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlplOuter.Controls.Add(this.tlpInner, 0, 1);
            this.tlplOuter.Controls.Add(this.labelTema, 0, 0);
            this.tlplOuter.Controls.Add(this.ibOriginal, 0, 3);
            this.tlplOuter.Controls.Add(this.ibGrayscale, 1, 3);
            this.tlplOuter.Controls.Add(this.lblOriginalImg, 0, 2);
            this.tlplOuter.Controls.Add(this.label2, 1, 2);
            this.tlplOuter.Controls.Add(this.lblThreshold, 0, 4);
            this.tlplOuter.Controls.Add(this.lblRegioni, 1, 4);
            this.tlplOuter.Controls.Add(this.ibThreshold, 0, 5);
            this.tlplOuter.Controls.Add(this.ibRegioni, 1, 5);
            this.tlplOuter.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tlplOuter.Location = new System.Drawing.Point(0, 0);
            this.tlplOuter.Name = "tlplOuter";
            this.tlplOuter.RowCount = 6;
            this.tlplOuter.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tlplOuter.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tlplOuter.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tlplOuter.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlplOuter.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.tlplOuter.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlplOuter.Size = new System.Drawing.Size(991, 715);
            this.tlplOuter.TabIndex = 2;
            // 
            // tlpInner
            // 
            this.tlpInner.AutoSize = true;
            this.tlpInner.BackColor = System.Drawing.Color.Orange;
            this.tlpInner.ColumnCount = 3;
            this.tlplOuter.SetColumnSpan(this.tlpInner, 3);
            this.tlpInner.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.tlpInner.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tlpInner.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 832F));
            this.tlpInner.Controls.Add(this.buttonOpenFile, 0, 0);
            this.tlpInner.Controls.Add(this.buttonGrayscale, 1, 0);
            this.tlpInner.Controls.Add(this.lblChosenFile, 2, 0);
            this.tlpInner.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tlpInner.Location = new System.Drawing.Point(3, 16);
            this.tlpInner.Name = "tlpInner";
            this.tlpInner.RowCount = 1;
            this.tlpInner.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tlpInner.Size = new System.Drawing.Size(985, 29);
            this.tlpInner.TabIndex = 0;
            // 
            // lblChosenFile
            // 
            this.lblChosenFile.AutoSize = true;
            this.lblChosenFile.Location = new System.Drawing.Point(156, 0);
            this.lblChosenFile.Name = "lblChosenFile";
            this.lblChosenFile.Size = new System.Drawing.Size(29, 13);
            this.lblChosenFile.TabIndex = 1;
            this.lblChosenFile.Text = "label";
            this.lblChosenFile.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // buttonGrayscale
            // 
            this.buttonGrayscale.AutoSize = true;
            this.buttonGrayscale.Location = new System.Drawing.Point(84, 3);
            this.buttonGrayscale.Name = "buttonGrayscale";
            this.buttonGrayscale.Size = new System.Drawing.Size(64, 23);
            this.buttonGrayscale.TabIndex = 2;
            this.buttonGrayscale.Text = "Grayscale";
            this.buttonGrayscale.UseVisualStyleBackColor = true;
            // 
            // ibOriginal
            // 
            this.ibOriginal.BackColor = System.Drawing.Color.OldLace;
            this.ibOriginal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.ibOriginal.Dock = System.Windows.Forms.DockStyle.Fill;
            this.ibOriginal.Enabled = false;
            this.ibOriginal.Location = new System.Drawing.Point(3, 64);
            this.ibOriginal.Name = "ibOriginal";
            this.ibOriginal.Size = new System.Drawing.Size(489, 314);
            this.ibOriginal.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.ibOriginal.TabIndex = 2;
            this.ibOriginal.TabStop = false;
            // 
            // ibGrayscale
            // 
            this.ibGrayscale.BackColor = System.Drawing.Color.OldLace;
            this.ibGrayscale.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.ibGrayscale.Dock = System.Windows.Forms.DockStyle.Fill;
            this.ibGrayscale.Enabled = false;
            this.ibGrayscale.Location = new System.Drawing.Point(498, 64);
            this.ibGrayscale.Name = "ibGrayscale";
            this.ibGrayscale.Size = new System.Drawing.Size(490, 314);
            this.ibGrayscale.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.ibGrayscale.TabIndex = 2;
            this.ibGrayscale.TabStop = false;
            // 
            // lblOriginalImg
            // 
            this.lblOriginalImg.AutoSize = true;
            this.lblOriginalImg.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblOriginalImg.Location = new System.Drawing.Point(3, 48);
            this.lblOriginalImg.Name = "lblOriginalImg";
            this.lblOriginalImg.Size = new System.Drawing.Size(489, 13);
            this.lblOriginalImg.TabIndex = 3;
            this.lblOriginalImg.Text = "Originalna slika";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.label2.Location = new System.Drawing.Point(498, 48);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(490, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "Grayscale slika";
            // 
            // lblThreshold
            // 
            this.lblThreshold.AutoSize = true;
            this.lblThreshold.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblThreshold.Location = new System.Drawing.Point(3, 381);
            this.lblThreshold.Name = "lblThreshold";
            this.lblThreshold.Size = new System.Drawing.Size(489, 13);
            this.lblThreshold.TabIndex = 5;
            this.lblThreshold.Text = "Threshold (binary) slika";
            // 
            // lblRegioni
            // 
            this.lblRegioni.AutoSize = true;
            this.lblRegioni.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblRegioni.Location = new System.Drawing.Point(498, 381);
            this.lblRegioni.Name = "lblRegioni";
            this.lblRegioni.Size = new System.Drawing.Size(490, 13);
            this.lblRegioni.TabIndex = 6;
            this.lblRegioni.Text = "Regioni od interesa";
            // 
            // ibThreshold
            // 
            this.ibThreshold.BackColor = System.Drawing.Color.OldLace;
            this.ibThreshold.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.ibThreshold.Dock = System.Windows.Forms.DockStyle.Fill;
            this.ibThreshold.Enabled = false;
            this.ibThreshold.Location = new System.Drawing.Point(3, 397);
            this.ibThreshold.Name = "ibThreshold";
            this.ibThreshold.Size = new System.Drawing.Size(489, 315);
            this.ibThreshold.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.ibThreshold.TabIndex = 2;
            this.ibThreshold.TabStop = false;
            // 
            // ibRegioni
            // 
            this.ibRegioni.BackColor = System.Drawing.Color.OldLace;
            this.ibRegioni.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.ibRegioni.Dock = System.Windows.Forms.DockStyle.Fill;
            this.ibRegioni.Enabled = false;
            this.ibRegioni.Location = new System.Drawing.Point(498, 397);
            this.ibRegioni.Name = "ibRegioni";
            this.ibRegioni.Size = new System.Drawing.Size(490, 315);
            this.ibRegioni.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.ibRegioni.TabIndex = 2;
            this.ibRegioni.TabStop = false;
            // 
            // ofdOpenFile
            // 
            this.ofdOpenFile.FileName = "openFileDialog1";
            // 
            // formMainFrame
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.NavajoWhite;
            this.ClientSize = new System.Drawing.Size(991, 715);
            this.Controls.Add(this.tlplOuter);
            this.Name = "formMainFrame";
            this.ShowIcon = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Miloš Siđi RA 184/2012 SC";
            this.tlplOuter.ResumeLayout(false);
            this.tlplOuter.PerformLayout();
            this.tlpInner.ResumeLayout(false);
            this.tlpInner.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.ibOriginal)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.ibGrayscale)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.ibThreshold)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.ibRegioni)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button buttonOpenFile;
        private System.Windows.Forms.Label labelTema;
        private System.Windows.Forms.TableLayoutPanel tlplOuter;
        private System.Windows.Forms.TableLayoutPanel tlpInner;
        private System.Windows.Forms.Label lblChosenFile;
        private Emgu.CV.UI.ImageBox ibOriginal;
        private Emgu.CV.UI.ImageBox ibGrayscale;
        private System.Windows.Forms.OpenFileDialog ofdOpenFile;
        private System.Windows.Forms.Label lblOriginalImg;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button buttonGrayscale;
        private System.Windows.Forms.Label lblThreshold;
        private System.Windows.Forms.Label lblRegioni;
        private Emgu.CV.UI.ImageBox ibThreshold;
        private Emgu.CV.UI.ImageBox ibRegioni;
    }
}

