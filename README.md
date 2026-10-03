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

Core **26.0.4**, Umbrel integration **26.0.4-umbrel.1**.
The container image is pinned by SHA256 digest and supports linux/amd64 and linux/arm64.

Automated native Core, Docker/TUN, dashboard browser and package checks passed.
Installation, reboot and upgrade on a physical Umbrel device have not yet been verified.
Treat this initial integration as beta.

Source and implementation: https://github.com/Uqda/Core/pull/22

Setup, permissions, backups and validation limits:
https://github.com/Uqda/Core/blob/877ef28a0f465b2dea0effa471372a8751d0904a/docs/umbrel.md

The Core service uses host networking, NET_ADMIN and /dev/net/tun to create
the host IPv6 interface. The dashboard does not receive these privileges.
Services must listen on IPv6 and permit traffic through their firewall to
be reachable; installing this app does not automatically expose other Docker apps.
