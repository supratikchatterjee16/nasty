\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{srmreport}[2014/08/16 Example LaTeX class]
\LoadClass[12pt,a4paper]{report}
%graphicx,multicol,geometry,xcolor,sectsty,setspace,hyperref,url,color,amsmath,amssymbol,pifont,appendix,times,tikz,t1enc,subfigure,pgfplots,seqsplit,tocbibind
\RequirePackage{graphicx}
\RequirePackage{multicol}
\RequirePackage{geometry}
\RequirePackage{xcolor}
\RequirePackage{sectsty}
\RequirePackage{setspace}
\RequirePackage[bookmarks=true,pdfborder={0 0 0},hidelinks]{hyperref}
\RequirePackage{color}
\RequirePackage{amsmath}
\RequirePackage{fancyhdr}
\RequirePackage{amssymb}
\RequirePackage{pifont}
\RequirePackage{appendix}
\RequirePackage{times}
\RequirePackage{t1enc}
\RequirePackage{tikz}
\RequirePackage{csquotes}
\RequirePackage{subfigure}
\RequirePackage{pgfplots}
\RequirePackage{seqsplit}
\RequirePackage[nottoc,notlof,notlot]{tocbibind} 
\RequirePackage[section]{placeins}
\RequirePackage{titlesec}

\renewcommand\bibname{References}

\chapterfont{\centering}
\geometry{a4paper,portrait, top=2cm,bottom=2cm,left=3cm,right=2cm}

\titleformat{\chapter}[display]
  { \huge}
  {\centering\bfseries\MakeUppercase{ \chaptertitlename } { \thechapter }} {2 pt}{\centering\MakeUppercase\bfseries\huge}

\newcommand*{\topic}[1]{\gdef\@topic{#1}}
\newcommand*{\@topic}{}
\let\Topic\@topic

\newcommand*{\second}[1]{\gdef\@second{#1}}
\newcommand*{\@second}{}
\let\Second\@second

\newcommand*{\third}[1]{\gdef\@third{#1}}
\newcommand*{\@third}{}
\let\Third\@third

\newcommand*{\desc}[1]{\gdef\@desc{#1}}
\newcommand*{\@desc}{}
\let\Desc\@desc

\newcommand*{\guide}[1]{\gdef\@guide{#1}}
\newcommand*{\@guide}{}
\let\Guide\@guide

\newcommand*{\obj}[1]{\gdef\@obj{#1}}
\newcommand*{\@obj}{}
\let\Obj\@obj

\newcommand*{\hod}[1]{\gdef\@hod{#1}}
\newcommand*{\@hod}{}
\let\Hod\@hod

\renewcommand*{\abstract}[1]{\gdef\@abstract{#1}}
\newcommand*{\@abstract}{}

\newcommand*{\dept}[1]{\gdef\@dept{#1}}
\newcommand*{\@dept}{}
\let\Dept\@Dept

\newcommand*{\bonafide}[1]{\gdef\@bonafide{#1}}
\newcommand*{\@bonafide}{}

\let\thanks\undefined
\let\@thanks\undefined
\newcommand*{\thanks}[1]{\gdef\@thanks{#1}}
\newcommand*{\@thanks}{}

\renewcommand{\maketitle}{
\begin{titlepage}
\centering
\vspace*{\fill}
{
{\Large\bfseries\MakeUppercase\@topic  - \MakeUppercase\@desc\\}
\vspace{0.4cm}
{\large\bfseries A\\\vspace{0.4cm}\MakeUppercase\@obj\\}

\vspace*{1cm}
{\large\bfseries Submitted by\\
\MakeUppercase\@author\\\MakeUppercase\@second\\\MakeUppercase\@third\\}
\vspace{1.5cm}
\textit{\bfseries Under the guidance of\\}\vspace{0.2cm}
{\large\bfseries Mr. Muthurasu N., B.E., M.Tech.,\\}\vspace{0.2cm}
\textit{(Assistant professor, Department of \@dept)\\\vspace{0.2cm}\bfseries in partial fulfilment of the degree\\Of\\}\vspace{0.8cm}
{\large\bfseries BACHELOR OF TECHNOLOGY}\\\vspace{0.4cm}
\textit{in}\\\vspace{0.4cm}
{\large\bfseries \MakeUppercase\@dept}\\\vspace{0.4cm}
\textit{of}\\\vspace{0.4cm}
{\large\bfseries FACULTY OF ENGINEERING AND TECHNOLOGY}\\\vspace{0.4cm}
\begin{figure}[h]
\centering
\includegraphics[scale=0.6]{SRMlogo}
\end{figure}
{\large
SRM  INSTITUTE OF TECHNOLOGY AND SCIENCE\\
Vadapalani, Chennai-600026\\\vspace{0.4cm}
{\bfseries\MakeUppercase\@date\null}}
}
\vspace*{\fill}
\end{titlepage}
\begin{titlepage}
\centering
\vspace*{\fill}
{
{\Large\bfseries\MakeUppercase\@topic  - \MakeUppercase\@desc\\}
\vspace{0.4cm}
{\large\bfseries A\\\vspace{0.4cm}\MakeUppercase\@obj\\}

\vspace*{1cm}
{\large\bfseries Submitted by\\
\MakeUppercase\@author\\\MakeUppercase\@second\\\MakeUppercase\@third\\}
\vspace{1.5cm}
\textit{\bfseries Under the guidance of\\}\vspace{0.2cm}
{\large\bfseries Mr. Muthurasu N., B.E., M.Tech.,\\}\vspace{0.2cm}
\textit{(Assistant professor, Department of \@dept)\\\vspace{0.2cm}\bfseries in partial fulfilment of the degree\\Of\\}\vspace{0.8cm}
{\large\bfseries BACHELOR OF TECHNOLOGY}\\\vspace{0.4cm}
\textit{in}\\\vspace{0.4cm}
{\large\bfseries \MakeUppercase\@dept}\\\vspace{0.4cm}
\textit{of}\\\vspace{0.4cm}
{\large\bfseries FACULTY OF ENGINEERING AND TECHNOLOGY}\\\vspace{0.4cm}
\begin{figure}[h]
\centering
\includegraphics[scale=0.6]{SRMlogo}
\end{figure}
{\large
SRM  INSTITUTE OF TECHNOLOGY AND SCIENCE\\
Vadapalani, Chennai-600026\\\vspace{0.4cm}
{\bfseries\MakeUppercase\@date\null}}
}
\vspace*{\fill}
\end{titlepage}
\pagenumbering{roman}
\addcontentsline{toc}{chapter}{Foreword}
%   \vspace*{\fill}
\begin{figure}
\hfill\includegraphics[scale=0.6]{SRMlogo}
\end{figure}
\vspace{2cm}
{\centering\Large\bfseries BONAFIDE CERTIFICATE\\}
\EnableQuotes
\addcontentsline{toc}{section}{Bonafide Certificate}
\vspace*{2cm}
\large
It is certified that this project report titled "\@topic" is the bonafide work of {\bfseries\large\@bonafide\hspace{0.1cm}}, who carried out the project work under my supervision.
%\end{doublespacing}
\vspace*{6.5cm}
\setlength{\columnsep}{150pt}
\begin{multicols}{2}
\noindent {\bfseries Signature of the Guide\\\\\\} \@guide
\columnbreak

\noindent{\bfseries Signature of the HOD\\\\\\}\@hod
\end{multicols}
\vspace*{\fill}
\newpage
\vspace*{\fill}
{\centering\huge\bfseries Acknowledgement\\}
\vspace*{1cm}
\large\@thanks
\vspace*{\fill}
\newpage
\large
\vspace*{\fill}
{\centering\huge\bfseries Abstract\\}
\vspace*{1cm}
\@abstract
\addcontentsline{toc}{section}{Abstract}
\vspace*{\fill}
\addcontentsline{toc}{section}{Acknowledgment}
\vspace*{\fill}
\newpage
\tableofcontents
\addcontentsline{toc}{section}{Table of Contents}
\newpage
%\listoftables
%\addcontentsline{toc}{section}{List of Tables}
\listoffigures
\addcontentsline{toc}{section}{List of Figures}
\newpage
\pagenumbering{arabic}
}
