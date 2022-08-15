%global debug_package %{nil}

Name:           storcli
Version:        007.2203.0000.0000
Release:        1%{?dist}
Summary:        Broadcom MegaRAID StorCLI
License:        Proprietary
URL:            https://www.broadcom.com/products/storage/raid-controllers
ExclusiveArch:  aarch64 x86_64 ppc64le

# Search at: https://www.broadcom.com/support/download-search?pg=&pf=&pn=&pa=&po=&dk=storcli&pl=
Source0:        https://docs.broadcom.com/docs-and-downloads/raid-controllers/raid-controllers-common-files/%{version}_Unified_StorCLI.zip
Source1:        https://docs.broadcom.com/docs-and-downloads/raid-controllers/raid-controllers-common-files/%{version}_Unified_StorCLI.txt

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

%ifnarch ppc64le
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
%endif

%prep
%autosetup -n Unified_storcli_all_os
cp %{SOURCE1} changelog.txt
unzip -q JSON-Schema/JSON_SCHEMA_FILES.zip

%ifarch x86_64
rpm2cpio Linux/*rpm | cpio -idm
mv opt/MegaRAID/storcli/storcli64 .
cp EFI/storcli.efi .
%endif

%ifarch aarch64
unzip ARM/Linux/storcli64.zip
cp ARM/EFI/storcli.efi .
%endif

%ifarch ppc64le
unzip Linux-PPC/LittleEndian/storcli64.zip
%endif

%build
# Nothing to build

%install
install -p -m 0755 -D %{name}64 %{buildroot}%{_sbindir}/%{name}
%ifnarch ppc64le
install -p -m 0644 -D %{name}.efi %{buildroot}%{efi_esp_efi}/%{name}.efi
%endif

%files
%license ThirdPartyLicenseNotice.pdf
%doc changelog.txt readme.txt storcliconf.ini JSON-Schema
%{_sbindir}/%{name}

%ifnarch ppc64le
%files efi
%{efi_esp_efi}/%{name}.efi
%endif

%changelog
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
