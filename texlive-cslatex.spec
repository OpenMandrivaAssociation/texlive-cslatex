# revision 23409
# category Package
# catalog-ctan /macros/cstex/base/cslatex.tar.gz
# catalog-date 2009-09-24 20:53:04 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-cslatex
Version:	20090924
Release:	4
Summary:	LaTeX support for Czech/Slovak typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/cstex/base/cslatex.tar.gz
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cslatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cslatex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cslatex.source.tar.xz
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
%{_texmfdistdir}/tex/cslatex/base/cslatex-utf8.ini
%{_texmfdistdir}/tex/cslatex/base/cslatex.ini
%{_texmfdistdir}/tex/cslatex/base/cspsfont.il2
%{_texmfdistdir}/tex/cslatex/base/cspsfont.tex
%{_texmfdistdir}/tex/cslatex/base/cspsfont.xl2
%{_texmfdistdir}/tex/cslatex/base/fonttext.cfg
%{_texmfdistdir}/tex/cslatex/base/hyphen.cfg
%{_texmfdistdir}/tex/cslatex/base/il2pag.fd
%{_texmfdistdir}/tex/cslatex/base/il2pbk.fd
%{_texmfdistdir}/tex/cslatex/base/il2pcr.fd
%{_texmfdistdir}/tex/cslatex/base/il2phv.fd
%{_texmfdistdir}/tex/cslatex/base/il2phvn.fd
%{_texmfdistdir}/tex/cslatex/base/il2pnc.fd
%{_texmfdistdir}/tex/cslatex/base/il2ppl.fd
%{_texmfdistdir}/tex/cslatex/base/il2ptm.fd
%{_texmfdistdir}/tex/cslatex/base/il2pzc.fd
%{_texmfdistdir}/tex/cslatex/base/nhelvet.sty
%{_texmfdistdir}/tex/cslatex/base/ntimes.sty
%{_texmfdistdir}/tex/cslatex/base/xl2pag.fd
%{_texmfdistdir}/tex/cslatex/base/xl2pbk.fd
%{_texmfdistdir}/tex/cslatex/base/xl2pcr.fd
%{_texmfdistdir}/tex/cslatex/base/xl2phv.fd
%{_texmfdistdir}/tex/cslatex/base/xl2phvn.fd
%{_texmfdistdir}/tex/cslatex/base/xl2pnc.fd
%{_texmfdistdir}/tex/cslatex/base/xl2ppl.fd
%{_texmfdistdir}/tex/cslatex/base/xl2ptm.fd
%{_texmfdistdir}/tex/cslatex/base/xl2pzc.fd
%{_texmfdistdir}/tex/latex/cslatex/il2cmdh.fd
%{_texmfdistdir}/tex/latex/cslatex/il2cmfib.fd
%{_texmfdistdir}/tex/latex/cslatex/il2cmfr.fd
%{_texmfdistdir}/tex/latex/cslatex/il2cmr.fd
%{_texmfdistdir}/tex/latex/cslatex/il2cmss.fd
%{_texmfdistdir}/tex/latex/cslatex/il2cmtt.fd
%{_texmfdistdir}/tex/latex/cslatex/il2cmvtt.fd
%{_texmfdistdir}/tex/latex/cslatex/il2enc.def
%{_texmfdistdir}/tex/latex/cslatex/il2lcmss.fd
%{_texmfdistdir}/tex/latex/cslatex/il2lcmtt.fd
%_texmf_fmtutil_d/cslatex
%doc %{_texmfdistdir}/doc/cslatex/base/INSTALL.cslatex
%doc %{_texmfdistdir}/doc/cslatex/base/README-cspsfont
%doc %{_texmfdistdir}/doc/cslatex/base/README.cslatex
%doc %{_texmfdistdir}/doc/cslatex/base/cs-fonts.doc
%doc %{_texmfdistdir}/doc/cslatex/base/cscorr.tab
%doc %{_texmfdistdir}/doc/cslatex/base/csplain.doc
%doc %{_texmfdistdir}/doc/cslatex/base/license.eng
%doc %{_texmfdistdir}/doc/cslatex/base/mklinks
%doc %{_texmfdistdir}/doc/cslatex/base/parpozn.tex
%doc %{_texmfdistdir}/doc/cslatex/base/prvni.tex
%doc %{_texmfdistdir}/doc/cslatex/base/test8z.tex
%doc %{_texmfdistdir}/doc/cslatex/base/testlat.tex
%doc %{_texmfdistdir}/doc/cslatex/base/zmeny.txt
#- source
%doc %{_texmfdistdir}/source/cslatex/base/cslatex.dtx
%doc %{_texmfdistdir}/source/cslatex/base/cslatex.ins
%doc %{_texmfdistdir}/source/cslatex/base/cslatex.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/cslatex <<EOF
#
# from cslatex:
cslatex pdftex - -etex -translate-file=cp227.tcx cslatex.ini
pdfcslatex pdftex - -etex -translate-file=cp227.tcx cslatex.ini
EOF


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090924-3
+ Revision: 778431
- Rebuild after tlpobj2spec.pl bug correction.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090924-2
+ Revision: 750656
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090924-1
+ Revision: 718171
- texlive-cslatex
- texlive-cslatex
- texlive-cslatex
- texlive-cslatex

