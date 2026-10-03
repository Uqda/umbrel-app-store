# Uqda Community App Store

Install Uqda Network on Umbrel with an Arabic/English dashboard.

## Install

1. Open Umbrel's App Store and select Community App Stores.
2. Add **https://github.com/Uqda/umbrel-app-store**.
3. Open **Uqda Network** and select **Install**.
4. Open the app and sign in with the app password shown by Umbrel.
5. Add a trusted peer and the same strong group password used by your other Uqda nodes.

## التثبيت

1. افتح متجر التطبيقات في Umbrel ثم Community App Stores.
2. أضف الرابط: https://github.com/Uqda/umbrel-app-store
3. اختر Uqda Network واضغط Install.
4. افتح التطبيق واستخدم كلمة المرور التي يعرضها Umbrel.
5. أضف عنوان نظير موثوق وكلمة مرور المجموعة المشتركة مع عقدك الأخرى.

New nodes start isolated. Configuration and node identity persist in app data.
Keep protected backups; do not run two active nodes with the same identity.

## Version and validation

Core **26.0.4**, Umbrel integration **26.0.4-umbrel.2**.
The container image is pinned by SHA256 digest and supports linux/amd64 and linux/arm64.

Automated native amd64/arm64 Docker/TUN, browser, package and two-node TCP/UDP
checks passed. The official Umbrel 2.0 development app manager passed installation,
restart, previous-wrapper-to-new-source upgrade and uninstall/fresh-install tests.
Production OS boot/reboot, backup restoration, full owner-browser gateway flow,
external storage and Raspberry Pi firmware remain unverified. A production VM
can test these without buying hardware; development Docker is not OS certification.

## Update and use

Back up app data, refresh the community store and update Uqda Network through
Umbrel. Identity and group settings persist across updates and restarts. Deleting
app data removes the identity. New installations remain isolated until a trusted
peer and matching strong group password are configured. A green transport peer
does not establish end-to-end group connectivity: test the other node, then the
intended IPv6 service and its firewall separately.

This release protects dashboard reads and changes with a tab-held, origin-scoped
session proof. A cookie alone received by another co-hosted app cannot recover
the proof or read status. Reloading the same tab retains access; new tabs may
require login again. Use HTTPS when available: plain HTTP does not protect
browser passwords in transit. Uqda does not provide anonymity.

للتحديث: انسخ بيانات التطبيق احتياطيًا، حدّث المتجر ثم التطبيق من Umbrel.
تبقى هوية العقدة وإعدادات المجموعة محفوظة. الحذف الكامل يمسح الهوية.
الإصدار الجديد يحسّن حماية الجلسة وحفظ الإعدادات وإخفاء البيانات الحساسة.
اربط عقدة موثوقة بنفس كلمة مرور المجموعة، واختبر الاتصال ثم الخدمة المطلوبة.
اختبارات Docker ومدير Umbrel الرسمي نجحت؛ إقلاع النظام الإنتاجي واستعادة
النسخ الاحتياطية لم يُختبرا. هذا تحديث لتكامل Umbrel وليس للنواة أو Homebrew.

Source and implementation: https://github.com/Uqda/Core/pull/22

Setup, permissions, backups and validation limits:
https://github.com/Uqda/Core/blob/877ef28a0f465b2dea0effa471372a8751d0904a/docs/umbrel.md

The Core service uses host networking, NET_ADMIN and /dev/net/tun to create
the host IPv6 interface. The dashboard does not receive these privileges.
Services must listen on IPv6 and permit traffic through their firewall to
be reachable; installing this app does not automatically expose other Docker apps.
