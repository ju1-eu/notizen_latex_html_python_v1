\ProvidesClass{vorlage-design-main}[2024/02/01 Angepasste Klasse für Artikel]

%\newif\if@suppmat\@suppmattrue
%\DeclareOption{nosupp}{\@suppmatfalse}
\ProcessOptions\relax
\ExecuteOptions{}
\LoadClass[twoside,11pt]{article}
\RequirePackage{graphicx}
\RequirePackage{etoolbox}
%\RequirePackage{regexpatch}
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
  \RequirePackage[libertine]{newtxmath}
  \RequirePackage[no-math]{fontspec}
  \setmainfont{TeX Gyre Termes}
  \setmonofont{Source Code Pro} % Für Quellcode
\else
  \RequirePackage[utf8]{inputenc}
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
%\RequirePackage{amssymb,amsmath,amsthm,amsfonts}

\geometry{
  paperwidth=20.99cm,       % Papierbreite
  paperheight=29.70cm,      % Papierhöhe
  top=2.54cm,               % Oberer Rand, kann angepasst werden, um die Erhöhung von headheight auszugleichen
  bottom=1.905cm,           % Unterer Rand
  inner=1.905cm,            % Innerer Rand (zum Binden)
  outer=1.524cm,            % Äußerer Rand
  headsep=0.762cm,          % Abstand zwischen Kopfzeile und Text
  footskip=0.762cm,         % Abstand zwischen Fußzeile und Text
  footnotesep=1.016cm,      % Abstand zwischen dem Textkörper und den Fußnoten
  reversemarginpar,         % Vertauscht die Seitenränder für Randnotizen
  marginparwidth=1.4605cm,  % Breite der Randnotizen
  marginparsep=0.5em,       % Abstand zwischen Randnotizen und Text unverändert
}

% Anpassen des oberen Randes, um die Erhöhung der Kopfzeilenhöhe auszugleichen
% Gesamtbild des Dokuments beizubehalten
\addtolength{\topmargin}{-1.6pt}
\setlength{\headheight}{13.6pt} % Anpassen der Kopfzeilenhöhe




\newcommand{\runningtitle}[1]{\def\@runningtitle{#1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\@name{\@author}
\def\@jahr{\the\year}
\def\@journalname{Notizen}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\RequirePackage{tikz}

% Titel 1
%\renewcommand{\@maketitle}{%
%  \begingroup\raggedright%
%  \rule{\textwidth}{1pt}\par
%  {\LARGE\bfseries\@title\par}
%  %\medskip
%  %{\Large\@author\par\vspace*{1em}}
%  \medskip
%  {\Large\@date\par\vspace*{1em}}
%  \endgroup
%}
% Titel 2
%\renewcommand{\@maketitle}{
%  % Startseite Farbe und Titelformatierung
%  \thispagestyle{firstpage} % Keine Kopf-/Fußzeilen auf dieser Seite
%  \noindent
%  \begin{center}
%    % Temporäres Erhöhen von \fboxsep, um den Innenabstand der colorbox zu vergrößern
%    \setlength{\fboxsep}{6pt} % Passe an Innenabstand zu erreichen
%    \colorbox{mydarkblue}{%
%      % Die Breite der parbox auf textwidth setzen
%      \parbox{\dimexpr\textwidth-2\fboxsep\relax}{%
%        \color{mydarkred}%
%        \vspace*{0.2em} % Vertikaler Abstand vor dem Titel
%        {\LARGE\bfseries\@title\par} % Titel
%        \medskip
%        {\Large\@date\par\vspace*{1em}}
%      }%
%    }
%    % Zurücksetzen von \fboxsep auf den Standardwert nach der Box
%    \setlength{\fboxsep}{3pt} % auf Standardwert
%  \end{center}
%}
% Titel 3
\renewcommand{\@maketitle}{
  \thispagestyle{empty} % Keine Kopf-/Fußzeilen auf dieser Seite
  \begin{tikzpicture}[remember picture,overlay]
    \node[anchor=north west, minimum width=\paperwidth, fill=mydarkblue] at (current page.north west) {
      \parbox{\textwidth}{
        \vspace*{5pt} % Abstand am Anfang der Box von oben
        {\color{webgrau}\LARGE\bfseries\@title\par} % Titel
        %\vspace{5pt} % Abstand zwischen Titel und Autor
        %{\color{mydarkred}\Large\@author\par} % Autor
        \vspace{1em} % Abstand zwischen Autor und Datum
        {\color{webrot}\Large\@date\par} % Datum
        \vspace{5pt} % Abstand am Ende der Box
      }
    };
  \end{tikzpicture}
  \vspace{3cm} % Stellt sicher, dass der Text nach der Box beginnt, Abstand ggf. anpassen
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
\newcommand{\floatnotes}[2][Anmerkungen: ]{%
  \par\medskip%
  \begingroup%
  \begin{minipage}{0.9\linewidth}
  \raggedright\footnotesize%
  \emph{#1}#2\par
  \end{minipage}\endgroup%
}

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

% v1.3: Oxford-Kommas
\AtBeginDocument{\renewcommand{\finalandcomma}{\addcomma}}

\setlength{\bibhang}{1em}
\renewcommand{\bibfont}{\small}
\setlength{\bibitemsep}{\z@}

%% Tabellen verwenden kleinere Schriftgrößen
\DeclareRobustCommand{\patchINOtable}[1]{%
  \BeforeBeginEnvironment{#1}{\footnotesize}
}
%% Tabellenlinien
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
%   \linenumbers
  \ifdefvoid{\@runningtitle}{\edef\@runningtitle{\@title}}{}
}


\RequirePackage{listings}
\lstset{
  basicstyle=\ttfamily\small,      % Verwendet eine kleine Schriftgröße im typewriter Stil für den Code
  language=C,                   % Standardmäßige Programmiersprache
  breaklines=true,                 % Ermöglicht automatische Zeilenumbrüche
  %numbers=left,                    % Zeilennummern auf der linken Seite
  %numberstyle=\tiny\color{gray},   % Stil der Zeilennummern
  %stepnumber=1,                    % Jede Zeile wird nummeriert
  %numbersep=5pt,                   % Abstand zwischen Zeilennummern und Code
  %backgroundcolor=\color{white},   % Hintergrundfarbe des Codes
  showspaces=false,                % Zeigt Leerzeichen nicht speziell an
  showstringspaces=false,          % Zeigt Leerzeichen in Zeichenketten nicht speziell an
  showtabs=false,                  % Zeigt Tabs nicht speziell an
  %frame=single,                    % Fügt einen Rahmen um den Code hinzu
  %rulecolor=\color{black},         % Rahmenfarbe
  tabsize=4,                       % Tabulatorgröße
  captionpos=b,                    % Position der Beschriftung unten
  breakatwhitespace=false,         % Zeilenumbrüche auch mitten in Wörtern möglich
  title=\lstname,                  % Zeigt den Dateinamen des Codes als Titel
  keywordstyle=\bfseries\color{DarkSlateGray},% Stil der Schlüsselwörter
  commentstyle=\color{gray33},    % Stil der Kommentare
  stringstyle=\color{DarkOrange},       % Stil der Zeichenketten
  escapeinside={\%*}{*)},          % Ermöglicht LaTeX innerhalb Ihres Codes
  inputencoding=utf8,
  %morekeywords={*,...},            % Falls Sie zusätzliche Schlüsselwörter hervorheben möchten
  %deletekeywords={...}             % Falls Sie bestimmte Schlüsselwörter nicht hervorheben möchten
}

% Farbdefinitionen
% https://www.farb-tabelle.de/de/rgb2hex.htm?q=RoyalBlue
\RequirePackage{xcolor}
\definecolor{red3}{rgb}{0.80, 0, 0} % red3
\definecolor{blue3}{rgb}{0,0,0.80} % blue3
\definecolor{DodgerBlue4}{rgb}{0.06, 0.31, 0.55} % DodgerBlue4
\definecolor{DarkOrange}{rgb}{1.0, 0.55, 0} % DarkOrange
\definecolor{dunklesgrau}{rgb}{0.1, 0.1, 0.1} % gray1
\definecolor{ForestGreen}{rgb}{0.13, 0.55, 0.13} % ForestGreen
\definecolor{DarkSlateGray}{rgb}{0.18,0.31,0.31} % DarkSlateGray
\definecolor{gray33}{rgb}{0.33,0.33,0.33} % gray33
\definecolor{maroon4}{rgb}{0.55,0.11,0.38} % maroon4
% Web benutzerdefinierten Farben
\definecolor{mydarkblue}{HTML}{010625} % Dunkles Blau
\definecolor{mydarkred}{HTML}{a30404}  % Dunkles Rot
\definecolor{webheader}{HTML}{25383C}  % webheader  #25383C
\definecolor{webrot}{HTML}{B82328}     % webrot #B82328
\definecolor{webgrau}{HTML}{808080}    % webgrau #808080

\lstset{literate={á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1 {Á}{{\'A}}1 {É}{{\'E}}1 {Í}{{\'I}}1 {Ó}{{\'O}}1 {Ú}{{\'U}}1 {à}{{\`a}}1 {è}{{\`e}}1 {ì}{{\`i}}1 {ò}{{\`o}}1 {ù}{{\`u}}1 {À}{{\`A}}1 {È}{{\'E}}1 {Ì}{{\`I}}1 {Ò}{{\`O}}1 {Ù}{{\`U}}1 {ä}{{\"a}}1 {ë}{{\"e}}1 {ï}{{\"i}}1 {ö}{{\"o}}1 {ü}{{\"u}}1 {Ä}{{\"A}}1 {Ë}{{\"E}}1 {Ï}{{\"I}}1 {Ö}{{\"O}}1 {Ü}{{\"U}}1 {â}{{\^a}}1 {ê}{{\^e}}1 {î}{{\^i}}1 {ô}{{\^o}}1 {û}{{\^u}}1 {Â}{{\^A}}1 {Ê}{{\^E}}1 {Î}{{\^I}}1 {Ô}{{\^O}}1 {Û}{{\^U}}1 {œ}{{\oe}}1 {Œ}{{\OE}}1 {æ}{{\ae}}1 {Æ}{{\AE}}1 {ß}{{\ss}}1 {ű}{{\H{u}}}1 {Ű}{{\H{U}}}1 {ő}{{\H{o}}}1 {Ő}{{\H{O}}}1 {ç}{{\c c}}1 {Ç}{{\c C}}1 {ø}{{\o}}1 {å}{{\r a}}1 {Å}{{\r A}}1 {€}{{\EUR}}1 {£}{{\pounds}}1 {~}{{\textasciitilde}}1 {-}{{-}}1 }

\AtEndPreamble{
  \RequirePackage[hyperfootnotes=false]{hyperref}
}

\tolerance=2000
\emergencystretch=\maxdimen
\hyphenpenalty=10000
\hbadness=10000
