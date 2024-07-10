具体的な手順をステップ1から細かく説明します。

ステップ1: プロジェクトの作成
Visual Studioを起動し、[新しいプロジェクトの作成]をクリックします。
Windows フォーム アプリケーション (.NET Framework) を選択します。
プロジェクト名、場所、ソリューション名、フレームワークを設定します（添付画像の設定通りにしても問題ありません）。
[作成]をクリックしてプロジェクトを作成します。
ステップ2: フォームデザイン
ツールボックスからフォームに以下のコントロールをドラッグアンドドロップします:
Button（名前: showOptionsButton, テキスト: Show Options）
ComboBox（名前: comboBox1, 初期状態は Visible = false）
GroupBox（名前: groupBox1, 初期状態は Visible = false）
GroupBoxの中に RadioButton を3つ配置（名前: radioButton1, radioButton2, radioButton3、テキスト: Option A, Option B, Option C）
Button（名前: submitButton, テキスト: Submit, ComboBoxやRadioButtonの下に配置）
ステップ3: コードの追加
フォームのコードビハインドファイル（Form1.cs）を開きます。

using System;
using System.Windows.Forms;
using Microsoft.Office.Interop.PowerPoint;
using PowerPoint = Microsoft.Office.Interop.PowerPoint;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // コンボボックスとラジオボタンの初期設定
            comboBox1.Items.AddRange(new string[] { "Option 1", "Option 2", "Option 3" });
            radioButton1.Text = "Option A";
            radioButton2.Text = "Option B";
            radioButton3.Text = "Option C";
            comboBox1.Visible = false;
            groupBox1.Visible = false;
        }

        private void showOptionsButton_Click(object sender, EventArgs e)
        {
            // コンボボックスとラジオボタンを表示
            comboBox1.Visible = true;
            groupBox1.Visible = true;
        }

        private void submitButton_Click(object sender, EventArgs e)
        {
            string selectedText = "";

            // コンボボックスの選択項目を取得
            if (comboBox1.SelectedItem != null)
            {
                selectedText = comboBox1.SelectedItem.ToString();
            }

            // ラジオボタンの選択項目を取得
            if (radioButton1.Checked)
            {
                selectedText = radioButton1.Text;
            }
            else if (radioButton2.Checked)
            {
                selectedText = radioButton2.Text;
            }
            else if (radioButton3.Checked)
            {
                selectedText = radioButton3.Text;
            }

            if (!string.IsNullOrEmpty(selectedText))
            {
                // PowerPointに出力
                CreatePowerPoint(selectedText);
            }
        }

        private void CreatePowerPoint(string text)
        {
            PowerPoint.Application pptApp = new PowerPoint.Application();
            Presentation pptPresentation = pptApp.Presentations.Add(MsoTriState.msoTrue);
            Slides slides = pptPresentation.Slides;
            Slide slide = slides.Add(1, PpSlideLayout.ppLayoutText);
            TextRange objText = slide.Shapes[1].TextFrame.TextRange;
            objText.Text = text;

            pptApp.Visible = MsoTriState.msoTrue;
        }
    }
}
ステップ4: イベントハンドラの接続
フォームデザイナーで、各コントロールのイベントハンドラを接続します。
showOptionsButton の Click イベントに showOptionsButton_Click メソッドを接続します。
submitButton の Click イベントに submitButton_Click メソッドを接続します。
フォームの Load イベントに Form1_Load メソッドを接続します。
ステップ5: NuGetパッケージのインストール
ソリューションエクスプローラーでプロジェクトを右クリックし、[NuGet パッケージの管理]を選択します。
Microsoft.Office.Interop.PowerPoint パッケージを検索してインストールします。
以上の手順を実行すると、ボタンが押された際にセレクトボックスとラジオボタンが表示され、選択した項目がPowerPointに出力されるデスクトップアプリケーションが完成します。


ツールボックスが表示されていない場合は、以下の手順でツールボックスを表示することができます。

ツールボックスを表示する手順
Visual Studioのメニューバーから「表示」をクリックします。
ドロップダウンメニューから「ツールボックス」を選択します。
これにより、ツールボックスが表示されるはずです。もし表示されない場合は、以下の手順も試してみてください。

ツールボックスを再表示する手順
Visual Studioのメニューバーから「表示」をクリックします。
「ツールバー」を選択し、「標準」を選択します。
ツールバーが表示されたら、再度「表示」から「ツールボックス」を選択します。
これでツールボックスが表示されるはずです。

フォームにコントロールを配置する
ツールボックスが表示されたら、以下のコントロールをフォームにドラッグアンドドロップします：
Button（名前: showOptionsButton, テキスト: Show Options）
ComboBox（名前: comboBox1, 初期状態は Visible = false）
GroupBox（名前: groupBox1, 初期状態は Visible = false）
GroupBoxの中に RadioButton を3つ配置（名前: radioButton1, radioButton2, radioButton3、テキスト: Option A, Option B, Option C）
Button（名前: submitButton, テキスト: Submit, ComboBoxやRadioButtonの下に配置）
コントロールの配置後のコード追加
前述のコードをForm1.csに追加し、各イベントハンドラを設定します。具体的には、次の手順です：

フォームデザイナーで各コントロールを選択し、プロパティウィンドウでClickイベントに対応するイベントハンドラを設定します。
showOptionsButton の Click イベントに showOptionsButton_Click メソッドを接続。
submitButton の Click イベントに submitButton_Click メソッドを接続。
フォームの Load イベントに Form1_Load メソッドを接続。
これで、フォームに必要なコントロールを配置し、コードを追加する準備が整いました。次に進む際に問題が発生した場合は、教えてください。


コントロールの名前を設定する方法について説明します。Visual Studioでは、コントロールのプロパティウィンドウを使用して名前やテキストなどを設定することができます。

コントロールの名前とテキストの設定方法
フォームデザイナーで、名前を設定したいコントロール（例：Button1）をクリックして選択します。
プロパティウィンドウが通常、Visual Studioの右側に表示されます。もし表示されていない場合は、メニューの「表示」->「プロパティウィンドウ」を選択して表示させます。
プロパティウィンドウで「(Name)」プロパティを見つけます。このプロパティがコントロールの名前を設定する場所です。
「(Name)」プロパティに適切な名前（例：showOptionsButton）を入力します。
同じプロパティウィンドウで「Text」プロパティを見つけます。このプロパティがボタンの表示テキストを設定する場所です。
「Text」プロパティに表示したいテキスト（例：Show Options）を入力します。
各コントロールに対する具体的な設定例
showOptionsButton:

(Name) プロパティ: showOptionsButton
Text プロパティ: Show Options
comboBox1:

(Name) プロパティ: comboBox1
Visible プロパティ: false（初期状態で非表示）
groupBox1:

(Name) プロパティ: groupBox1

Visible プロパティ: false（初期状態で非表示）

内部の RadioButton:

radioButton1:
(Name) プロパティ: radioButton1
Text プロパティ: Option A
radioButton2:
(Name) プロパティ: radioButton2
Text プロパティ: Option B
radioButton3:
(Name) プロパティ: radioButton3
Text プロパティ: Option C
submitButton:

(Name) プロパティ: submitButton
Text プロパティ: Submit
手順を実行する際の参考画像
以下は、各プロパティを設定するためのプロパティウィンドウの例です（例：ボタンの場合）。



以上の手順を参考にして、コントロールの名前とテキストを設定してください。設定が完了したら、前述のコードをForm1.csに追加し、各イベントハンドラを設定します。


イベントハンドラを接続する方法について、具体的な手順を説明します。

イベントハンドラの接続方法
フォームデザイナーを表示:

Visual StudioでForm1.cs [デザイン]タブを選択してフォームデザイナーを開きます。
ボタンのイベントハンドラを接続:

フォームデザイナーで、showOptionsButtonをクリックして選択します。
プロパティウィンドウが右側に表示されていることを確認します。表示されていない場合は、メニューの「表示」->「プロパティウィンドウ」を選択します。
プロパティウィンドウの上部に、雷のアイコン（イベントタブ）があります。このアイコンをクリックします。
イベントの一覧が表示されますので、Clickイベントを見つけます。
Clickの隣の空白部分をダブルクリックします。これにより、showOptionsButton_Clickというイベントハンドラが自動的に作成されます。
他のボタンも同様に設定:

submitButtonについても同様に、プロパティウィンドウのイベントタブでClickイベントをダブルクリックして、submitButton_Clickというイベントハンドラを作成します。
フォームのLoadイベントを接続:

フォームデザイナーの空白部分（フォーム自体）をクリックして選択します。
プロパティウィンドウのイベントタブを開き、Loadイベントを見つけます。
Loadの隣の空白部分をダブルクリックします。これにより、Form1_Loadというイベントハンドラが自動的に作成されます。
イベントハンドラのコード追加
以下のコードをそれぞれのイベントハンドラに追加します。

csharp
コードをコピーする
// Form1_Loadイベントハンドラ
private void Form1_Load(object sender, EventArgs e)
{
    // コンボボックスとラジオボタンの初期設定
    comboBox1.Items.AddRange(new string[] { "Option 1", "Option 2", "Option 3" });
    radioButton1.Text = "Option A";
    radioButton2.Text = "Option B";
    radioButton3.Text = "Option C";
    comboBox1.Visible = false;
    groupBox1.Visible = false;
}

// showOptionsButton_Clickイベントハンドラ
private void showOptionsButton_Click(object sender, EventArgs e)
{
    // コンボボックスとラジオボタンを表示
    comboBox1.Visible = true;
    groupBox1.Visible = true;
}

// submitButton_Clickイベントハンドラ
private void submitButton_Click(object sender, EventArgs e)
{
    string selectedText = "";

    // コンボボックスの選択項目を取得
    if (comboBox1.SelectedItem != null)
    {
        selectedText = comboBox1.SelectedItem.ToString();
    }

    // ラジオボタンの選択項目を取得
    if (radioButton1.Checked)
    {
        selectedText = radioButton1.Text;
    }
    else if (radioButton2.Checked)
    {
        selectedText = radioButton2.Text;
    }
    else if (radioButton3.Checked)
    {
        selectedText = radioButton3.Text;
    }

    if (!string.IsNullOrEmpty(selectedText))
    {
        // PowerPointに出力
        CreatePowerPoint(selectedText);
    }
}

private void CreatePowerPoint(string text)
{
    PowerPoint.Application pptApp = new PowerPoint.Application();
    Presentation pptPresentation = pptApp.Presentations.Add(MsoTriState.msoTrue);
    Slides slides = pptPresentation.Slides;
    Slide slide = slides.Add(1, PpSlideLayout.ppLayoutText);
    TextRange objText = slide.Shapes[1].TextFrame.TextRange;
    objText.Text = text;

    pptApp.Visible = MsoTriState.msoTrue;
}
これでイベントハンドラが適切に接続され、ボタンがクリックされたときに対応する処理が実行されるようになります。


ChatGPT
エラーメッセージによると、comboBox1_SelectedIndexChangedというイベントハンドラが定義されていないために問題が発生しています。このイベントハンドラを追加する方法を説明します。

イベントハンドラの定義と接続方法
イベントハンドラの定義:
Form1.csに以下のコードを追加して、comboBox1_SelectedIndexChangedというイベントハンドラを定義します。
csharp
コードをコピーする
private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
{
    // イベントハンドラのコード（ここでは特に何もする必要はありません）
}
イベントハンドラの接続:
Form1.Designer.csファイルを開きます。エラーが発生している行を次のように修正します。
csharp
コードをコピーする
this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
完全なコード例
以下は、Form1.csとForm1.Designer.csに必要なすべてのコードを含む完全な例です。

Form1.cs
csharp
コードをコピーする
using System;
using System.Windows.Forms;
using Microsoft.Office.Interop.PowerPoint;
using PowerPoint = Microsoft.Office.Interop.PowerPoint;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // コンボボックスとラジオボタンの初期設定
            comboBox1.Items.AddRange(new string[] { "Option 1", "Option 2", "Option 3" });
            radioButton1.Text = "Option A";
            radioButton2.Text = "Option B";
            radioButton3.Text = "Option C";
            comboBox1.Visible = false;
            groupBox1.Visible = false;
        }

        private void showOptionsButton_Click(object sender, EventArgs e)
        {
            // コンボボックスとラジオボタンを表示
            comboBox1.Visible = true;
            groupBox1.Visible = true;
        }

        private void submitButton_Click(object sender, EventArgs e)
        {
            string selectedText = "";

            // コンボボックスの選択項目を取得
            if (comboBox1.SelectedItem != null)
            {
                selectedText = comboBox1.SelectedItem.ToString();
            }

            // ラジオボタンの選択項目を取得
            if (radioButton1.Checked)
            {
                selectedText = radioButton1.Text;
            }
            else if (radioButton2.Checked)
            {
                selectedText = radioButton2.Text;
            }
            else if (radioButton3.Checked)
            {
                selectedText = radioButton3.Text;
            }

            if (!string.IsNullOrEmpty(selectedText))
            {
                // PowerPointに出力
                CreatePowerPoint(selectedText);
            }
        }

        private void CreatePowerPoint(string text)
        {
            PowerPoint.Application pptApp = new PowerPoint.Application();
            Presentation pptPresentation = pptApp.Presentations.Add(MsoTriState.msoTrue);
            Slides slides = pptPresentation.Slides;
            Slide slide = slides.Add(1, PpSlideLayout.ppLayoutText);
            TextRange objText = slide.Shapes[1].TextFrame.TextRange;
            objText.Text = text;

            pptApp.Visible = MsoTriState.msoTrue;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            // コンボボックスの選択項目が変更されたときの処理（ここでは特に何もする必要はありません）
        }
    }
}
Form1.Designer.cs
csharp
コードをコピーする
namespace WindowsFormsApp1
{
    partial class Form1
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージド リソースを破棄する場合は true を指定し、アンマネージド リソースを破棄する場合は false を指定します。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.showOptionsButton = new System.Windows.Forms.Button();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.radioButton3 = new System.Windows.Forms.RadioButton();
            this.submitButton = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // showOptionsButton
            // 
            this.showOptionsButton.Location = new System.Drawing.Point(116, 52);
            this.showOptionsButton.Name = "showOptionsButton";
            this.showOptionsButton.Size = new System.Drawing.Size(121, 23);
            this.showOptionsButton.TabIndex = 0;
            this.showOptionsButton.Text = "Show Options";
            this.showOptionsButton.UseVisualStyleBackColor = true;
            this.showOptionsButton.Click += new System.EventHandler(this.showOptionsButton_Click);
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(116, 135);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(121, 20);
            this.comboBox1.TabIndex = 1;
            this.comboBox1.Visible = false;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.radioButton3);
            this.groupBox1.Controls.Add(this.radioButton2);
            this.groupBox1.Controls.Add(this.radioButton1);
            this.groupBox1.Location = new System.Drawing.Point(116, 175);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(200, 100);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Options";
            this.groupBox1.Visible = false;
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.Location = new System.Drawing.Point(17, 20);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(68, 16);
            this.radioButton1.TabIndex = 0;
            this.radioButton1.TabStop = true;
            this.radioButton1.Text = "Option A";
            this.radioButton1.UseVisualStyleBackColor = true;
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.Location = new System.Drawing.Point(17, 42);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(68, 16);
            this.radioButton2.TabIndex = 1;
            this.radioButton2.TabStop = true;
            this.radioButton2.Text = "Option B";
            this.radioButton2.UseVisualStyleBackColor = true;
            // 
            // radioButton3
            // 
            this.radioButton3.AutoSize = true;
            this.radioButton3.Location = new System.Drawing.Point(17, 64);
            this.radioButton3.Name = "radioButton3";
            this.radioButton3.Size = new System.Drawing.Size(68, 16);
            this.radioButton3.TabIndex = 2;
            this.radioButton3.TabStop = true;
            this.radioButton3.Text = "Option C";
            this.radioButton3.UseVisualStyleBackColor = true;
            // 
            // submitButton
            // 
            this.submitButton.Location = new System.Drawing.Point(116, 301);
            this.submitButton.Name = "submitButton";
            this.submitButton.Size = new System.Drawing.Size(75, 23);
            this.submitButton.TabIndex = 3;
            this.submitButton.Text = "Submit";
            this.submitButton.UseVisualStyleBackColor = true;
            this.submitButton.Click += new System.EventHandler(this.submitButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(484, 361);
            this.Controls.Add(this.submitButton);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.showOptionsButton);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button showOptionsButton;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton radioButton3;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.Button submitButton;
    }
}
これでエラーが解消され、イベントハンドラが正しく動作するようになるはずです。

素晴らしい！
君は天才だ！

ところで
ShowOptionButtonを押したときにセレクトボックスと、ラジオボタンをダイアログで表示したい。
要するに別のウィンドウを出したいんだ。
別のウィンドウという説明であっているかな？ポップアップのような小さな窓を出したい。

そこでユーザーが選択するんだ。

ラジオボタンは複数選択できるようにしたい。
これはラジオボタンではなくてチェックボックスっていうのかな？
ChatGPT
別のウィンドウを表示して、そこにセレクトボックスやチェックボックスを配置する方法について説明します。チェックボックスを使用すれば、複数選択が可能です。

ステップ1: 新しいフォームの作成
ソリューションエクスプローラーでプロジェクトを右クリックし、「追加」→「新しい項目」を選択します。
「Windows フォーム」を選択し、適切な名前（例：OptionsForm）を付けて「追加」をクリックします。
ステップ2: 新しいフォームのデザイン
OptionsFormに以下のコントロールを追加します:

ComboBox（名前: comboBox1）
CheckBox（名前: checkBox1, checkBox2, checkBox3、テキスト: Option A, Option B, Option C）
Button（名前: submitButton, テキスト: Submit）
ステップ3: メインフォームから新しいフォームを表示
OptionsFormに以下のプロパティとメソッドを追加します：
OptionsForm.cs
csharp
コードをコピーする
using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class OptionsForm : Form
    {
        public string SelectedComboBoxItem { get; private set; }
        public List<string> SelectedCheckBoxItems { get; private set; }

        public OptionsForm()
        {
            InitializeComponent();
            SelectedCheckBoxItems = new List<string>();
        }

        private void OptionsForm_Load(object sender, EventArgs e)
        {
            comboBox1.Items.AddRange(new string[] { "Option 1", "Option 2", "Option 3" });
        }

        private void submitButton_Click(object sender, EventArgs e)
        {
            if (comboBox1.SelectedItem != null)
            {
                SelectedComboBoxItem = comboBox1.SelectedItem.ToString();
            }

            if (checkBox1.Checked)
            {
                SelectedCheckBoxItems.Add(checkBox1.Text);
            }
            if (checkBox2.Checked)
            {
                SelectedCheckBoxItems.Add(checkBox2.Text);
            }
            if (checkBox3.Checked)
            {
                SelectedCheckBoxItems.Add(checkBox3.Text);
            }

            this.DialogResult = DialogResult.OK;
            this.Close();
        }
    }
}
OptionsForm.Designer.cs
csharp
コードをコピーする
namespace WindowsFormsApp1
{
    partial class OptionsForm
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.checkBox2 = new System.Windows.Forms.CheckBox();
            this.checkBox3 = new System.Windows.Forms.CheckBox();
            this.submitButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(12, 12);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(121, 21);
            this.comboBox1.TabIndex = 0;
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Location = new System.Drawing.Point(12, 50);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(70, 17);
            this.checkBox1.TabIndex = 1;
            this.checkBox1.Text = "Option A";
            this.checkBox1.UseVisualStyleBackColor = true;
            // 
            // checkBox2
            // 
            this.checkBox2.AutoSize = true;
            this.checkBox2.Location = new System.Drawing.Point(12, 74);
            this.checkBox2.Name = "checkBox2";
            this.checkBox2.Size = new System.Drawing.Size(70, 17);
            this.checkBox2.TabIndex = 2;
            this.checkBox2.Text = "Option B";
            this.checkBox2.UseVisualStyleBackColor = true;
            // 
            // checkBox3
            // 
            this.checkBox3.AutoSize = true;
            this.checkBox3.Location = new System.Drawing.Point(12, 98);
            this.checkBox3.Name = "checkBox3";
            this.checkBox3.Size = new System.Drawing.Size(70, 17);
            this.checkBox3.TabIndex = 3;
            this.checkBox3.Text = "Option C";
            this.checkBox3.UseVisualStyleBackColor = true;
            // 
            // submitButton
            // 
            this.submitButton.Location = new System.Drawing.Point(58, 130);
            this.submitButton.Name = "submitButton";
            this.submitButton.Size = new System.Drawing.Size(75, 23);
            this.submitButton.TabIndex = 4;
            this.submitButton.Text = "Submit";
            this.submitButton.UseVisualStyleBackColor = true;
            this.submitButton.Click += new System.EventHandler(this.submitButton_Click);
            // 
            // OptionsForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 161);
            this.Controls.Add(this.submitButton);
            this.Controls.Add(this.checkBox3);
            this.Controls.Add(this.checkBox2);
            this.Controls.Add(this.checkBox1);
            this.Controls.Add(this.comboBox1);
            this.Name = "OptionsForm";
            this.Text = "OptionsForm";
            this.Load += new System.EventHandler(this.OptionsForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.CheckBox checkBox2;
        private System.Windows.Forms.CheckBox checkBox3;
        private System.Windows.Forms.Button submitButton;
    }
}
ステップ4: メインフォームから新しいフォームを表示
Form1.cs
csharp
コードをコピーする
private void showOptionsButton_Click(object sender, EventArgs e)
{
    using (OptionsForm optionsForm = new OptionsForm())
    {
        if (optionsForm.ShowDialog() == DialogResult.OK)
        {
            string selectedComboBoxItem = optionsForm.SelectedComboBoxItem;
            List<string> selectedCheckBoxItems = optionsForm.SelectedCheckBoxItems;

            // 選択された項目を利用して処理を行う（例：PowerPointに出力）
            string result = "ComboBox: " + selectedComboBoxItem + "\nCheckBoxes: " + string.Join(", ", selectedCheckBoxItems);
            CreatePowerPoint(result);
        }
    }
}
これで、showOptionsButtonがクリックされたときに新しいフォームが表示され、ユーザーがセレクトボックスとチェックボックスで選択した項目を取得して処理することができます。

新しいフォーム（ポップアップ）でユーザーが項目を選択する方法は以上です。必要に応じて、各フォームのデザインや機能をカスタマイズしてください。
