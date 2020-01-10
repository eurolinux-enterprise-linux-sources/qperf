Name:           qperf
Summary:        Measure socket and RDMA performance
Version:        0.4.6
Release:        6%{?dist}
License:        GPLv2 or BSD
Group:          Networking/Diagnostic
Source: http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}-0.1.gb81434e.tar.gz
Patch0: qperf-0.4.4-noxrc.patch
Patch1: qperf-0.4.6-pf-define.patch
Url:            http://www.openfabrics.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libibverbs-devel >= 1.1.2-4, librdmacm-devel >= 1.0.8-5
ExclusiveArch:  %{ix86} x86_64 ia64 ppc ppc64
%description
Measure socket and RDMA performance.

%prep
%setup -q
%patch0 -p1 -b .noxrc
%patch1 -p1 -b .pf

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
%{__make}

%install
rm -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING
%_bindir/qperf
%_mandir/man1/qperf.1*

%changelog
* Thu Apr 05 2012 Doug Ledford <dledford@redhat.com> - 0.4.6-6
- Bump and rebuild to build against the right libibverbs
- Related: bz808673

* Thu Apr 05 2012 Doug Ledford <dledford@redhat.com> - 0.4.6-5
- Fix the fact that qperf was using the wrong PF_RDS define now that RDS
  is integrated upstream and its assigned number is no longer temporary
- Resolves: bz808673

* Fri Jan 06 2012 Doug Ledford <dledford@redhat.com> - 0.4.6-4
- Initial import into Fedora
- Bump and rebuild
- Related: bz739138

* Fri Jul 22 2011 Doug Ledford <dledford@redhat.com> - 0.4.6-3.el6
- Fix failure to build on i686
- Resolves: bz724899

* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 0.4.6-2.el6
- Cleanups for pkgwrangler import
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 0.4.6-1.el5
- Update to latest upstream version
- Related: bz518218

* Mon Jun 22 2009 Doug Ledford <dledford@redhat.com> - 0.4.4-3.el5
- Rebuild against libibverbs that isn't missing the proper ppc wmb() macro
- Related: bz506258

* Sun Jun 21 2009 Doug Ledford <dledford@redhat.com> - 0.4.4-2.el5
- Build against non-XRC libibverbs
- Update to ofed 1.4.1 final bits
- Related: bz506097, bz506258

* Sat Apr 18 2009 Doug Ledford <dledford@redhat.com> - 0.4.4-1.el5
- Update to ofed 1.4.1-rc3 version
- Related: bz459652

* Thu Sep 18 2008 Doug Ledford <dledford@redhat.com> - 0.4.1-2
- Add a build flag to silence some warnings

* Wed Sep 17 2008 Doug Ledford <dledford@redhat.com> - 0.4.1-1
- Update to the qperf tarball found in the OFED-1.4-beta1 tarball
- Resolves: bz451483

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 0.4.0-1
- Initial import to Red Hat repo management
- Related: bz428197

* Sat Oct 20 2007 - johann@georgex.org
- Initial package
