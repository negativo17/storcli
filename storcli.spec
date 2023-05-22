%global debug_package %{nil}

Name:           storcli
Version:        008.0005.0000.0010
Release:        1%{?dist}
Summary:        Broadcom MegaRAID StorCLI
License:        Proprietary
URL:            https://www.broadcom.com/products/storage/raid-controllers
ExclusiveArch:  aarch64 x86_64 ppc64le

# Search at: https://www.broadcom.com/support/download-search?pg=&pf=&pn=&pa=&po=&dk=storcli&pl=
# Note that final URLs, tarball name and tarball structure keep on changing.
Source0:        https://docs.broadcom.com/docs-and-downloads/%{version}_StorCLI.zip

%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires:  efi-srpm-macros
%else
%global efi_esp_efi /boot/efi/EFI
%endif

%description
MegaRAID StorageCli enables you to configure RAID controllers, monitor, maintain
storage configurations and it provides a range of functions, such as RAID array
configuration, RAID level migration, RAID array deletion, RAID information
import, and hard drive status adjustment.

MegaRAID StorCli provides a command line interface and does not support a GUI.

%package efi
Summary:        Broadcom MegaRAID StorCLI for UEFI
Requires:       efi-filesystem
Requires:       %{name}%{?_isa}

%description efi
MegaRAID StorageCli enables you to configure RAID controllers, monitor, maintain
storage configurations and it provides a range of functions, such as RAID array
configuration, RAID level migration, RAID array deletion, RAID information
import, and hard drive status adjustment.

This package contains a binary that can be executed from the EFI partition in a
UEFI environment.

%prep
%autosetup -c
unzip -q Avenger_StorCLI/JSON_Schema/JSON_SCHEMA_FILES.zip

%ifarch x86_64
rpm2cpio Avenger_StorCLI/Linux/*rpm | cpio -idm
mv opt/MegaRAID/storcli2/storcli2 .
cp Avenger_StorCLI/UEFI/storcli2.efi .
%endif

%ifarch aarch64
rpm2cpio Avenger_StorCLI/ARM/Linux/storcli2-008.0005.0000.0010-1.aarch64.rpm | cpio -idm
mv opt/MegaRAID/storcli2/storcli2 .
mv Avenger_StorCLI/ARM/UEFI/storcli2.efi .
%endif

%build
# Nothing to build

%install
install -p -m 0755 -D %{name}2 %{buildroot}%{_sbindir}/%{name}2
install -p -m 0644 -D %{name}2.efi %{buildroot}%{efi_esp_efi}/%{name}2.efi

%files
%license Avenger_StorCLI/ThirdPartyLicenseNotice.pdf
%doc Avenger_StorCLI/readme.txt Avenger_StorCLI/storcli2conf.ini Avenger_StorCLI/JSON_Schema/JSON_SCHEMA_FILES.zip
%{_sbindir}/%{name}2

%files efi
%{efi_esp_efi}/%{name}2.efi

%changelog
* Mon May 22 2023 Simone Caronni <negativo17@gmail.com> - 008.0005.0000.0010-1
- Update to 008.0005.0000.0010.
- Drop ppc64le builds.

* Fri Mar 24 2023 Simone Caronni <negativo17@gmail.com> - 007.2408.0000.0000-1
- Update to 007.2408.0000.0000.

* Thu Nov 10 2022 Simone Caronni <negativo17@gmail.com> - 007.2309.0000.0000-1
- Update to 007.2309.0000.000.

* Mon Aug 15 2022 Simone Caronni <negativo17@gmail.com> - 007.2203.0000.0000-1
- Update to 007.2203.0000.0000.

* Thu May 19 2022 Simone Caronni <negativo17@gmail.com> - 007.2106.0000.0000-1
- Update to 007.2106.0000.0000.

* Fri Mar 25 2022 Simone Caronni <negativo17@gmail.com> - 007.2007.0000.0000-1
- Update to version 007.2007.0000.0000.
- Allow building on ppc64le.

* Thu Dec 09 2021 Simone Caronni <negativo17@gmail.com> - 007.1912.0000.0000-1
- Update to 007.1912.0000.0000.

* Wed Nov 03 2021 Simone Caronni <negativo17@gmail.com> - 007.1907.0000.0000-1
- Update to 007.1907.0000.0000.

* Sat Jul 24 2021 Simone Caronni <negativo17@gmail.com> - 007.1804.0000.0000-1
- Update to 007.1804.0000.0000.

* Fri Feb 05 2021 Simone Caronni <negativo17@gmail.com> - 007.1613.0000.0000-1
- First build.
