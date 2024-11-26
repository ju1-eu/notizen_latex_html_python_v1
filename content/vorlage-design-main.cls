\ProvidesClass{vorlage-design-main}[2024/08/27 Angepasste Klasse für Artikel]

\ProcessOptions\relax
\ExecuteOptions{}
\LoadClass[twoside,11pt]{article}
\RequirePackage{graphicx}
\RequirePackage{etoolbox}
\RequirePackage{ifxetex,ifluatex}

\newif\ifxetexorluatex
\ifxetex
  \xetexorluatextrue
\else
  \ifluatex
    \xetexorluatextrue
  \else
    \xetexorluatexfalse
  \fi
\fi

\RequirePackage{microtype}

\ifxetexorluatex
  \RequirePackage[no-math]{fontspec}
  \setmainfont[
    Path = /Users/jan/Library/Fonts/,
    BoldFont = texgyretermes-bold.otf,
    ItalicFont = texgyretermes-italic.otf,
    BoldItalicFont = texgyretermes-bolditalic.otf
  ]{texgyretermes-regular.otf}
  \setmonofont{Source Code Pro}
  \usepackage{unicode-math}
  \setmathfont{texgyretermes-math.otf}
\else
  \RequirePackage[T1]{fontenc}
  \RequirePackage{newtxtext,newtxmath}
\fi

\RequirePackage[ngerman]{babel}
\RequirePackage{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage[medium,small,raggedright,noindentafter]{titlesec}
\RequirePackage[runin]{abstract}
\RequirePackage{booktabs}
\RequirePackage{caption,subcaption}
\RequirePackage{flafter}
\RequirePackage[norule,multiple]{footmisc}
\RequirePackage{enumitem}
\RequirePackage[figuresright]{rotating}
\RequirePackage{lineno}
\RequirePackage{url}
\RequirePackage{multicol,multirow}
\RequirePackage{eurosym}
\RequirePackage{tikz}
\usetikzlibrary{mindmap,trees}
\RequirePackage{pdfpages}

\geometry{
  paperwidth=20.99cm,
  paperheight=29.70cm,
  top=2.54cm,
  bottom=1.905cm,
  inner=1.905cm,
  outer=1.524cm,
  headsep=0.762cm,
  footskip=0.762cm,
  footnotesep=1.016cm,
  reversemarginpar,
  marginparwidth=1.4605cm,
  marginparsep=0.5em,
}

\addtolength{\topmargin}{-1.6pt}
\setlength{\headheight}{13.6pt}

\newcommand{\runningtitle}[1]{\def\@runningtitle{#1}}
\def\@name{\@author}
\def\@jahr{\the\year}
\def\@journalname{Notizen}

\RequirePackage{tikz}
\renewcommand{\@maketitle}{
  \thispagestyle{empty}
  \begin{tikzpicture}[remember picture,overlay]
    \node[anchor=north west, minimum width=\paperwidth, fill=mydarkblue] at (current page.north west) {
      \parbox{\textwidth}{
        \vspace*{5pt}
        {\color{webgrau}\LARGE\bfseries\@title\par}
        \vspace{1em}
        {\color{webrot}\Large\@date\par}
        \vspace{5pt}
      }
    };
  \end{tikzpicture}
  \vspace{3cm}
}

\renewcommand{\maketitle}{\vspace*{\dimexpr-\headsep-\baselineskip}\@maketitle\thispagestyle{firstpage}}

\titlespacing{name=\section}{0pt}{2\baselineskip}{\baselineskip}
\titlespacing{name=\section,numberless}{0pt}{2\baselineskip}{0.5em}

\fancyhf{}
\renewcommand{\headrulewidth}{1pt}
\fancyhead[RO]{\@runningtitle\quad\textbf{\thepage}}
\fancyhead[LE]{\textbf{\thepage}\quad\@journalname}
\pagestyle{fancy}
\fancypagestyle{firstpage}{%
  \fancyhf{}
  \renewcommand{\headrule}{}
  \fancyfoot[L]{\footnotesize~\\\textcopyright\space\@name, \@jahr}
  \fancyfoot[R]{\footnotesize~\\Seite \thepage\ von \pageref{LastPage}}
}

\setlength{\abstitleskip}{-\parindent}
\abslabeldelim{\quad}
\setlength{\absleftindent}{1em}
\setlength{\absrightindent}{1em}
\preto{\abstract}{%
  {\noindent\rule{\textwidth}{1pt}}\vspace*{1em}%
}
\appto{\endabstract}{%
  \vspace*{1em}%
  {\noindent\raisebox{1em}{\rule{\textwidth}{1pt}}}\vspace*{\baselineskip}
}

\setcounter{secnumdepth}{0}
\setlist{nosep,leftmargin=*,align=left,widest=00}
\newenvironment{authorbio}{\setlength{\parindent}{\z@}}{}

\captionsetup*{labelfont={bf,footnotesize},textfont={it},labelsep={period},justification=centering,singlelinecheck=false}
\captionsetup*[figure]{name=ABB.}
\captionsetup*[table]{name=TAB.,position=top,justification=raggedright}

\RequirePackage{csquotes}
\RequirePackage[backend=biber,authordate,autocite=footnote,dashed=false,isbn=false,language=german]{biblatex-chicago}
\ExecuteBibliographyOptions[jurisdiction,legal,legislation]{skipbib=false}
\DeclareFieldFormat[article]{title}{#1\isdot}
\DeclareFieldFormat[incollection]{title}{#1\isdot}
\DeclareFieldFormat[inbook]{title}{#1\isdot}
\DeclareFieldFormat[report]{title}{#1\isdot}
\DeclareFieldFormat[inproceedings]{title}{#1\isdot}
\DeclareFieldFormat[inproceedings]{booktitle}{#1\isdot}
\DeclareFieldFormat[thesis]{title}{#1\isdot}
\DeclareFieldFormat[misc]{title}{#1\isdot}
\DeclareFieldFormat{url}{Verfügbar unter <\url{#1}>}
\DefineBibliographyStrings{german}{%
  in = {\ifentrytype{inproceedings}{Vortrag bei}{In}},
}
\AtEveryBibitem{%
  \ifentrytype{book}{%
    \clearlist{location}%
    \clearfield{pages}%
  }{}
}
\urlstyle{same}

\AtBeginDocument{\renewcommand{\finalandcomma}{\addcomma}}

\setlength{\bibhang}{1em}
\renewcommand{\bibfont}{\small}
\setlength{\bibitemsep}{\z@}

\DeclareRobustCommand{\patchINOtable}[1]{%
  \BeforeBeginEnvironment{#1}{\footnotesize}
}

\renewcommand{\belowrulesep}{1em}
\renewcommand{\aboverulesep}{1em}
\setlength{\heavyrulewidth}{1pt}
\AtBeginDocument{%
  \patchINOtable{tabular}
  \patchINOtable{tabular*}
  \patchINOtable{sidewaystable}
  \patchINOtable{sidewaystable*}
  \@ifpackageloaded{tabularx}{\patchINOtable{tabularx}}{}
  \@ifpackageloaded{supertabular}{\patchINOtable{supertabular}}{}
  \@ifpackageloaded{longtable}{\patchINOtable{longtable}\setlength{\LTleft}{\z@}}{}
  \ifdefvoid{\@runningtitle}{\edef\@runningtitle{\@title}}{}
}

\RequirePackage{listings}
\lstset{
  basicstyle=\ttfamily\small,
  language=C,
  breaklines=true,
  showspaces=false,
  showstringspaces=false,
  showtabs=false,
  tabsize=4,
  captionpos=b,
  breakatwhitespace=false,
  title=\lstname,
  keywordstyle=\bfseries\color{DarkSlateGray},
  commentstyle=\color{gray33},
  stringstyle=\color{DarkOrange},
  escapeinside={\%*}{*)},
  inputencoding=utf8,
}

\RequirePackage{xcolor}
\definecolor{red3}{rgb}{0.80, 0, 0}
\definecolor{blue3}{rgb}{0,0,0.80}
\definecolor{DodgerBlue4}{rgb}{0.06, 0.31, 0.55}
\definecolor{DarkOrange}{rgb}{1.0, 0.55, 0}
\definecolor{dunklesgrau}{rgb}{0.1, 0.1, 0.1}
\definecolor{ForestGreen}{rgb}{0.13, 0.55, 0.13}
\definecolor{DarkSlateGray}{rgb}{0.18,0.31,0.31}
\definecolor{gray33}{rgb}{0.33,0.33,0.33}
\definecolor{maroon4}{rgb}{0.55,0.11,0.38}
\definecolor{mydarkblue}{HTML}{010625}
\definecolor{mydarkred}{HTML}{a30404}
\definecolor{webheader}{HTML}{25383C}
\definecolor{webrot}{HTML}{B82328}
\definecolor{webgrau}{HTML}{808080}

\lstset{literate={á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1 {Á}{{\'A}}1 {É}{{\'E}}1 {Í}{{\'I}}1 {Ó}{{\'O}}1 {Ú}{{\'U}}1 {à}{{\`a}}1 {è}{{\`e}}1 {ì}{{\`i}}1 {ò}{{\`o}}1 {ù}{{\`u}}1 {À}{{\`A}}1 {È}{{\'E}}1 {Ì}{{\`I}}1 {Ò}{{\`O}}1 {Ù}{{\`U}}1 {ä}{{\"a}}1 {ë}{{\"e}}1 {ï}{{\"i}}1 {ö}{{\"o}}1 {ü}{{\"u}}1 {Ä}{{\"A}}1 {Ë}{{\"E}}1 {Ï}{{\"I}}1 {Ö}{{\"O}}1 {Ü}{{\"U}}1 {â}{{\^a}}1 {ê}{{\^e}}1 {î}{{\^i}}1 {ô}{{\^o}}1 {û}{{\^u}}1 {Â}{{\^A}}1 {Ê}{{\^E}}1 {Î}{{\^I}}1 {Ô}{{\^O}}1 {Û}{{\^U}}1 {œ}{{\oe}}1 {Œ}{{\OE}}1 {æ}{{\ae}}1 {Æ}{{\AE}}1 {ß}{{\ss}}1 {ű}{{\H{u}}}1 {Ű}{{\H{U}}}1 {ő}{{\H{o}}}1 {Ő}{{\H{O}}}1 {ç}{{\c c}}1 {Ç}{{\c C}}1 {ø}{{\o}}1 {å}{{\r a}}1 {Å}{{\r A}}1 {€}{{\EUR}}1 {£}{{\pounds}}1 {~}{{\textasciitilde}}1 {-}{{-}}1 }

\AtEndPreamble{
  \RequirePackage[hyperfootnotes=false]{hyperref}
}

\tolerance=2000
\emergencystretch=\maxdimen
\hyphenpenalty=10000
\hbadness=10000
