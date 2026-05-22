What is a cryptographic inventory?
**********************************


A cryptographic inventory is a descriptive record of the cryptography used across an organization's systems, applications, services, devices, and data flows. It helps an organization identify where and how cryptography is being used so that cryptographic risks can be managed, policies can be applied consistently, and systems can be prepared for migration to post-quantum cryptography \(PQC\).

A cryptographic inventory may include information about:

⁃ Cryptographic algorithms in use, such as RSA, elliptic curve cryptography \(ECC\), AES, SHA-2, or post-quantum algorithms
⁃ Cryptographic protocols and services, such as TLS, SSH, VPNs, code signing, email encryption, and certificate-based authentication
⁃ Cryptographic keys, including key type, owner, associated algorithm, application, expiration date, and lifecycle status, without including the key material itself
⁃ Certificates and certificate chains
⁃ Systems, applications, or components that depend on cryptography
⁃ Data protected by cryptography, especially sensitive or long-lived data that may be vulnerable to “harvest now, decrypt later” threats

Related terms include **cryptographic algorithm inventory**, which focuses specifically on the algorithms in use, and **cryptographic assets**, which may include algorithms, keys, certificates, protocols, libraries, hardware security modules \(HSMs\), and other components that provide or depend on cryptographic protection.

Maintaining a cryptographic inventory is an important step in quantum readiness because organizations cannot effectively prioritize or migrate cryptography that they have not identified.