他のファイルのクラスで `Form` の描画したものの幅や高さを取得する方法として、以下のような方法があります。

1. **プロパティを使用して必要な情報を公開する**
2. **`Form` のインスタンスを他のクラスに渡す**
3. **イベントを使用して情報を通知する**

最も一般的で簡単な方法は、プロパティを使用して必要な情報を公開し、`Form` のインスタンスを他のクラスに渡す方法です。以下に具体的な例を示します。

### 1. プロパティを使用して必要な情報を公開する

#### CustomImageViewer.cs (Form クラス)

```csharp
using System;
using System.Drawing;
using System.Windows.Forms;

public partial class CustomImageViewer : Form
{
    public CustomImageViewer()
    {
        InitializeComponent();
        this.Paint += new PaintEventHandler(this.CustomImageViewer_Paint);
    }

    private void CustomImageViewer_Paint(object sender, PaintEventArgs e)
    {
        Graphics g = e.Graphics;
        int formWidth = this.ClientSize.Width;
        int formHeight = this.ClientSize.Height;
        int centerX = formWidth / 2;
        int centerY = formHeight / 2;
        Pen pen = new Pen(Color.Black, 2);
        g.DrawLine(pen, centerX, 0, centerX, formHeight);
        g.DrawLine(pen, 0, centerY, formWidth, centerY);
    }

    // 中央のX座標を取得するプロパティ
    public int CenterX
    {
        get { return this.ClientSize.Width / 2; }
    }

    // 中央のY座標を取得するプロパティ
    public int CenterY
    {
        get { return this.ClientSize.Height / 2; }
    }
}
```

### 2. Form のインスタンスを他のクラスに渡す

#### OtherClass.cs (他のクラス)

```csharp
using System;

public class OtherClass
{
    private CustomImageViewer customImageViewer;

    public OtherClass(CustomImageViewer customImageViewer)
    {
        this.customImageViewer = customImageViewer;
    }

    public void UseCenterCoordinates()
    {
        int centerX = this.customImageViewer.CenterX;
        int centerY = this.customImageViewer.CenterY;

        Console.WriteLine("中央のX座標: " + centerX);
        Console.WriteLine("中央のY座標: " + centerY);
    }
}
```

### 3. イベントを使用して情報を通知する（必要に応じて）

他のクラスに情報を通知するためにイベントを使用する方法もありますが、これは必要に応じて採用してください。

#### CustomImageViewer.cs (Form クラスにイベントを追加)

```csharp
public event EventHandler<CenterCoordinatesEventArgs> CenterCoordinatesChanged;

protected virtual void OnCenterCoordinatesChanged(CenterCoordinatesEventArgs e)
{
    EventHandler<CenterCoordinatesEventArgs> handler = CenterCoordinatesChanged;
    if (handler != null)
    {
        handler(this, e);
    }
}

private void CustomImageViewer_Paint(object sender, PaintEventArgs e)
{
    Graphics g = e.Graphics;
    int formWidth = this.ClientSize.Width;
    int formHeight = this.ClientSize.Height;
    int centerX = formWidth / 2;
    int centerY = formHeight / 2;
    Pen pen = new Pen(Color.Black, 2);
    g.DrawLine(pen, centerX, 0, centerX, formHeight);
    g.DrawLine(pen, 0, centerY, formWidth, centerY);

    OnCenterCoordinatesChanged(new CenterCoordinatesEventArgs(centerX, centerY));
}
```

#### CenterCoordinatesEventArgs.cs (カスタムイベント引数クラス)

```csharp
using System;

public class CenterCoordinatesEventArgs : EventArgs
{
    public int CenterX { get; private set; }
    public int CenterY { get; private set; }

    public CenterCoordinatesEventArgs(int centerX, int centerY)
    {
        CenterX = centerX;
        CenterY = centerY;
    }
}
```

#### OtherClass.cs (他のクラスでイベントをハンドリング)

```csharp
using System;

public class OtherClass
{
    private CustomImageViewer customImageViewer;

    public OtherClass(CustomImageViewer customImageViewer)
    {
        this.customImageViewer = customImageViewer;
        this.customImageViewer.CenterCoordinatesChanged += CustomImageViewer_CenterCoordinatesChanged;
    }

    private void CustomImageViewer_CenterCoordinatesChanged(object sender, CenterCoordinatesEventArgs e)
    {
        Console.WriteLine("中央のX座標: " + e.CenterX);
        Console.WriteLine("中央のY座標: " + e.CenterY);
    }
}
```

### プログラムの起動部分

```csharp
using System;
using System.Windows.Forms;

public static class Program
{
    [STAThread]
    static void Main()
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);

        CustomImageViewer customImageViewer = new CustomImageViewer();
        OtherClass otherClass = new OtherClass(customImageViewer);

        customImageViewer.Show();
        otherClass.UseCenterCoordinates();

        Application.Run(customImageViewer);
    }
}
```

このようにして、フォームの描画したものの幅や高さを他のクラスで取得する方法として、プロパティを使用する方法やイベントを使用する方法を取ることができます。具体的な要件に応じて、適切な方法を選択してください

using System;
using System.Drawing;
using System.Windows.Forms;

public partial class CustomImageViewer : Form
{
    private static CustomImageViewer _instance;

    public static CustomImageViewer Instance
    {
        get
        {
            if (_instance == null)
            {
                _instance = new CustomImageViewer();
            }
            return _instance;
        }
    }

    private CustomImageViewer()
    {
        InitializeComponent();
        this.Paint += new PaintEventHandler(this.CustomImageViewer_Paint);
    }

    private void CustomImageViewer_Paint(object sender, PaintEventArgs e)
    {
        Graphics g = e.Graphics;
        int formWidth = this.ClientSize.Width;
        int formHeight = this.ClientSize.Height;
        int centerX = formWidth / 2;
        int centerY = formHeight / 2;
        Pen pen = new Pen(Color.Black, 2);
        g.DrawLine(pen, centerX, 0, centerX, formHeight);
        g.DrawLine(pen, 0, centerY, formWidth, centerY);
    }

    // 中央のX座標を取得するプロパティ
    public int CenterX
    {
        get { return this.ClientSize.Width / 2; }
    }

    // 中央のY座標を取得するプロパティ
    public int CenterY
    {
        get { return this.ClientSize.Height / 2; }
    }
}
