Name:		texlive-lua-widow-control
Version:	65084
Release:	1
Summary:	Automatically remove widows and orphans from any document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lua-widow-control
License:	other-free cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-widow-control.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-widow-control.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-widow-control.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Unmodified TeX has very few ways of preventing widows and
orphans. In documents with figures, section headings, and
equations, TeX can stretch the vertical glue between items in
order to prevent widows and orphans, but many documents have no
figures or headings. TeX can also shorten the page by 1 line,
but this will give each page a different length which can make
a document look uneven. The typical solution is to
strategically insert \looseness=1, but this requires manual
editing every time that the document is edited.
Lua-widow-control is essentially an automation of the
\looseness method: it uses Lua callbacks to find "stretchy"
paragraphs, then it lengthens them to remove widows and
orphans. Lua-widow-control is compatible with all LuaTeX-based
formats. All that is required is to load the package at the
start of your document. To load: Plain LuaTeX: \input
lua-widow-control LuaLaTeX: \usepackage{lua-widow-control}
ConTeXt: \usemodule[lua-widow-control] OpTeX:
\load[lua-widow-control]

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/luatex/lua-widow-control
%{_texmfdistdir}/tex/optex/lua-widow-control
%{_texmfdistdir}/tex/luatex/lua-widow-control
%{_texmfdistdir}/tex/lualatex/lua-widow-control
%{_texmfdistdir}/tex/context/third/lua-widow-control
%doc %{_texmfdistdir}/doc/luatex/lua-widow-control

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
