# revision 28596
# category Package
# catalog-ctan /macros/cstex/base/cslatex.tar.gz
# catalog-date 2012-04-25 13:09:32 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-cslatex
Version:	20120425
Release:	7
Summary:	LaTeX support for Czech/Slovak typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/cstex/base/cslatex.tar.gz
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cslatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cslatex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires(post):	texlive-csplain
Requires:	texlive-latex
Requires:	texlive-cslatex.bin

%description
TeXLive cslatex package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/cslatex/base/cslatex.ini
%{_texmfdistdir}/tex/cslatex/base/czech.sty
%{_texmfdistdir}/tex/cslatex/base/fonttext.cfg
%{_texmfdistdir}/tex/cslatex/base/hyphen.cfg
%{_texmfdistdir}/tex/cslatex/base/il2cmdh.fd
%{_texmfdistdir}/tex/cslatex/base/il2cmfib.fd
%{_texmfdistdir}/tex/cslatex/base/il2cmfr.fd
%{_texmfdistdir}/tex/cslatex/base/il2cmr.fd
%{_texmfdistdir}/tex/cslatex/base/il2cmss.fd
%{_texmfdistdir}/tex/cslatex/base/il2cmtt.fd
%{_texmfdistdir}/tex/cslatex/base/il2cmvtt.fd
%{_texmfdistdir}/tex/cslatex/base/il2enc.def
%{_texmfdistdir}/tex/cslatex/base/il2lcmss.fd
%{_texmfdistdir}/tex/cslatex/base/il2lcmtt.fd
%{_texmfdistdir}/tex/cslatex/base/slovak.sty
%{_texmfdistdir}/tex/cslatex/cspsfonts/cspsfont.il2
%{_texmfdistdir}/tex/cslatex/cspsfonts/cspsfont.tex
%{_texmfdistdir}/tex/cslatex/cspsfonts/cspsfont.xl2
%{_texmfdistdir}/tex/cslatex/cspsfonts/il2pag.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/il2pbk.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/il2pcr.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/il2phv.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/il2phvn.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/il2pnc.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/il2ppl.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/il2ptm.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/il2pzc.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/nhelvet.sty
%{_texmfdistdir}/tex/cslatex/cspsfonts/ntimes.sty
%{_texmfdistdir}/tex/cslatex/cspsfonts/xl2pag.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/xl2pbk.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/xl2pcr.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/xl2phv.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/xl2phvn.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/xl2pnc.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/xl2ppl.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/xl2ptm.fd
%{_texmfdistdir}/tex/cslatex/cspsfonts/xl2pzc.fd
%_texmf_fmtutil_d/cslatex
#- source
%doc %{_texmfdistdir}/source/cslatex/base/cslatex.dtx
%doc %{_texmfdistdir}/source/cslatex/base/cslatex.ins

%doc %{_texmfdistdir}/source/cslatex/cspsfonts/cspsfont.doc
%doc %{_texmfdistdir}/source/cslatex/cspsfonts/cspsfont.drv

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/cslatex <<EOF
#
# from cslatex:
cslatex pdftex - -etex cslatex.ini
pdfcslatex pdftex - -etex cslatex.ini
EOF
