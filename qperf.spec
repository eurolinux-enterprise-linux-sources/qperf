Name:           qperf
Summary:        Measure socket and RDMA performance
Version:        0.4.9
Release:        1%{?dist}
License:        GPLv2 or BSD
Group:          Networking/Diagnostic
Url:            http://www.openfabrics.org

Source: http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libibverbs-devel >= 1.1.2-4, librdmacm-devel >= 1.0.8-5
ExcludeArch:    s390 s390x

%description
Measure socket and RDMA performance.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc COPYING
%_bindir/qperf
%_mandir/man1/qperf.1*

%changelog
* Thu Aug 01 2013 Doug Ledford <dledford@redhat.com> - 0.4.9-1
- Update to latest upstream release
- Drop no longer needed patches

* Mon Feb 18 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.6-8
- Build on ARM, modernise spec

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Doug Ledford <dledford@redhat.com> - 0.4.6-6
- Fix the fact that qperf was using the wrong PF_RDS define now that RDS
  is integrated upstream and its assigned number is no longer temporary

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 06 2012 Doug Ledford <dledford@redhat.com> - 0.4.6-4
- Initial import into Fedora

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
