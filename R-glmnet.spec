%global packname  glmnet
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.9.5
Release:          1
Summary:          Lasso and elastic-net regularized generalized linear models
Group:            Sciences/Mathematics
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.9-5.tar.gz

Requires:         R-Matrix R-utils 

Requires:         R-survival R-foreach 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Matrix R-utils

BuildRequires:   R-survival R-foreach 
%description
Extremely efficient procedures for fitting the entire lasso or elastic-net
regularization path for linear regression, logistic and multinomial
regression models, poisson regression and the Cox model. Two recent
additions are the multiresponse gaussian, and the grouped multinomial. The
algorithm uses cyclical coordinate descent in a pathwise fashion, as
described in the paper listed below.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/mortran
