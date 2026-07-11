%global tl_name lua-widow-control
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.1
Release:	%{tl_revision}.1
Summary:	Automatically remove widows and orphans from any document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/lua-widow-control
License:	other-free cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-widow-control.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-widow-control.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-widow-control.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Unmodified TeX has very few ways of preventing widows and orphans. In
documents with figures, section headings, and equations, TeX can stretch
the vertical glue between items in order to prevent widows and orphans,
but many documents have no figures or headings. TeX can also shorten the
page by 1 line, but this will give each page a different length which
can make a document look uneven. The typical solution is to
strategically insert \looseness=1, but this requires manual editing
every time that the document is edited. Lua-widow-control is essentially
an automation of the \looseness method: it uses Lua callbacks to find
"stretchy" paragraphs, then it lengthens them to remove widows and
orphans. Lua-widow-control is compatible with all LuaTeX and LuaMetaTeX-
based formats. All that is required is to load the package at the start
of your document. To load: Plain LuaTeX: \input lua-widow-control
LuaLaTeX: \usepackage{lua-widow-control} ConTeXt: \usemodule[lua-widow-
control] OpTeX: \load[lua-widow-control]

