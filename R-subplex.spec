#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-subplex
Version  : 1.6
Release  : 28
URL      : https://cran.r-project.org/src/contrib/subplex_1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/subplex_1.6.tar.gz
Summary  : Unconstrained Optimization using the Subplex Algorithm
Group    : Development/Tools
License  : GPL-3.0
Requires: R-subplex-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-subplex package.
Group: Libraries

%description lib
lib components for the R-subplex package.


%prep
%setup -q -c -n subplex
cd %{_builddir}/subplex

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589534415

%install
export SOURCE_DATE_EPOCH=1589534415
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library subplex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library subplex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library subplex
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc subplex || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/subplex/DESCRIPTION
/usr/lib64/R/library/subplex/GPL
/usr/lib64/R/library/subplex/INDEX
/usr/lib64/R/library/subplex/Meta/Rd.rds
/usr/lib64/R/library/subplex/Meta/features.rds
/usr/lib64/R/library/subplex/Meta/hsearch.rds
/usr/lib64/R/library/subplex/Meta/links.rds
/usr/lib64/R/library/subplex/Meta/nsInfo.rds
/usr/lib64/R/library/subplex/Meta/package.rds
/usr/lib64/R/library/subplex/NAMESPACE
/usr/lib64/R/library/subplex/NEWS
/usr/lib64/R/library/subplex/NEWS.Rd
/usr/lib64/R/library/subplex/R/subplex
/usr/lib64/R/library/subplex/R/subplex.rdb
/usr/lib64/R/library/subplex/R/subplex.rdx
/usr/lib64/R/library/subplex/help/AnIndex
/usr/lib64/R/library/subplex/help/aliases.rds
/usr/lib64/R/library/subplex/help/paths.rds
/usr/lib64/R/library/subplex/help/subplex.rdb
/usr/lib64/R/library/subplex/help/subplex.rdx
/usr/lib64/R/library/subplex/html/00Index.html
/usr/lib64/R/library/subplex/html/R.css
/usr/lib64/R/library/subplex/tests/ripple.R
/usr/lib64/R/library/subplex/tests/ripple.Rout.save
/usr/lib64/R/library/subplex/tests/rosen.R
/usr/lib64/R/library/subplex/tests/rosen.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/subplex/libs/subplex.so
/usr/lib64/R/library/subplex/libs/subplex.so.avx2
/usr/lib64/R/library/subplex/libs/subplex.so.avx512
