%define modname labltk
%define srcname labltk

Summary:	Tk interface for OCaml
Name:		ocaml-%{modname}
Version:	8.06.5
Release:	2
License:	BSD
Group:		Development/Other
Url:		https://forge.ocamlcore.org/projects/lablgl/
Source0:	https://forge.ocamlcore.org/frs/download.php/1764/labltk-%{version}.tar.gz
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(tk)
BuildRequires:	pkgconfig(xmu)

%description
LablTK is is an OCaml interface to Tcl/Tk.

%files
%{_bindir}/ocamlbrowser
%dir %{_libdir}/ocaml/labltk
%{_libdir}/ocaml/labltk/*.cmi
%{_libdir}/ocaml/labltk/*.cma
%{_libdir}/ocaml/labltk/*.cmo
%{_libdir}/ocaml/labltk/labltktop
%{_libdir}/ocaml/labltk/pp
%{_libdir}/ocaml/labltk/tkcompiler
%{_libdir}/ocaml/labltk/META
%{_libdir}/ocaml/stublibs/*.so
%{_bindir}/labltk

#----------------------------------------------------------------------------

%package devel
Summary:	Tcl/Tk interface for OCaml
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Requires:	pkgconfig(gl)
Requires:	pkgconfig(glu)
Requires:	pkgconfig(glut)
Requires:	pkgconfig(xmu)
Requires:	pkgconfig(tk)

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%{_libdir}/ocaml/labltk/*.a
%{_libdir}/ocaml/labltk/*.cmx
%{_libdir}/ocaml/labltk/*.cmxa
%{_libdir}/ocaml/labltk/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n %{modname}-%{version}
# Named like autoconf, but isn't
./configure

%build
make all opt

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/ocaml/labltk
install -d -m 755 %{buildroot}%{_libdir}/ocaml/stublibs
make \
   BINDIR=%{buildroot}%{_bindir} \
   INSTALLDIR=%{buildroot}%{_libdir}/ocaml/labltk \
   STUBLIBDIR=%{buildroot}%{_libdir}/ocaml/stublibs \
   install

rm -f %{buildroot}%{_libdir}/ocaml/labltk/*.ml

# Make and install a META file.
cat > %{buildroot}%{_libdir}/ocaml/labltk/META<<EOF
version="%{version}"
directory="+labltk"
archive(byte) = "labltk.cma"
archive(native) = "labltk.cmxa"
EOF
