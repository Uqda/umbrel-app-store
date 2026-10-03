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

Core **26.0.5**, Umbrel integration **26.0.5-umbrel.1**.
The container image is pinned by SHA256 digest and supports linux/amd64 and linux/arm64.

Automated native amd64/arm64 Docker/TUN, browser, package and two-node TCP/UDP
checks passed. The official Umbrel 2.0 development app manager passed installation,
restart, previous-public-wrapper-to-new-public-wrapper upgrade and uninstall/fresh-install tests.
Production OS boot/reboot, backup restoration, complete owner-browser interactions,
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

## Your Umbrel from another device

Connect another device running Uqda to the same private group. Copy the Umbrel
IPv6 address from the new private-access section, open it in that device's browser,
and sign in to Umbrel normally. Umbrel keeps its accounts, permissions and app
gateway. The service address book provides deliberate addresses and diagnostic
commands for existing HTTPS/HTTP/SSH/TCP services; it does not install or publish
apps. Local TCP listening is labelled separately from actual remote access.

This is a community integration, not official Umbrel endorsement or a complete
replacement for every Tailscale function. A browser alone does not create a Uqda
tunnel on a phone. Ready-made mobile clients, native Umbrel app integration,
verified HTTPS identity, SMB and backups require separate development/tests.
Do not disable certificate validation or remove a working alternative prematurely.

اربط جهاز الوصول بعقدة وبنفس المجموعة الخاصة، ثم افتح عنوان Umbrel الذي تعرضه
لوحة عقدة وسجّل دخولك إلى Umbrel كالمعتاد. دليل الخدمات يعرض عناوين وأوامر فحص
لخدماتك الموجودة، ولا يثبت التطبيقات أو يفتح منافذها. الهاتف وHTTPS والملفات
والنسخ الاحتياطي لها حدود واختبارات إضافية؛ هذا تكامل مجتمعي وليس اعتمادًا رسميًا.

للتحديث: انسخ بيانات التطبيق احتياطيًا، حدّث المتجر ثم التطبيق من Umbrel.
تبقى هوية العقدة وإعدادات المجموعة محفوظة. الحذف الكامل يمسح الهوية.
الإصدار الجديد يضيف الوصول إلى واجهة Umbrel ودليل الخدمات، مع حماية الجلسة
وحفظ الإعدادات وإخفاء البيانات الحساسة.
اربط عقدة موثوقة بنفس كلمة مرور المجموعة، واختبر الاتصال ثم الخدمة المطلوبة.
اختبارات Docker ومدير Umbrel الرسمي نجحت؛ إقلاع النظام الإنتاجي واستعادة
النسخ الاحتياطية لم يُختبرا. الحزمة تستخدم Core 26.0.5، الذي نُشر بصورة مستقلة
ويصلح تطبيق كلمة مرور المجموعة داخل SDK الهاتف؛ SDK ليس تطبيق VPN جاهزًا.

Source and implementation: https://github.com/Uqda/Core/pull/23

Setup, permissions, backups and validation limits:
https://github.com/Uqda/Core/blob/main/docs/umbrel-remote-access.md

Release notes, installable ZIP, checksums and actual dashboard screenshots:
https://github.com/Uqda/Core/releases/tag/umbrel-26.0.5-1

Exact published-image lifecycle and previous-to-current upgrade evidence:
https://github.com/Uqda/Core/actions/runs/37144854154
Earlier source-platform evidence: https://github.com/Uqda/Core/actions/runs/37141401980

The Core service uses host networking, NET_ADMIN and /dev/net/tun to create
the host IPv6 interface. The dashboard does not receive these privileges.
Services must listen on IPv6 and permit traffic through their firewall to
be reachable; installing this app does not automatically expose other Docker apps.
