What are some existing open source tools that can be used for cryptographic inventorying?
*****************************************************************************************

Open source tools
+++++++++++++++++++++

*   `pqcscan <https://github.com/anvilsecure/pqcscan>`_ for scanning SSH and TLS servers
*   `sslscan2 <https://github.com/rbsec/sslscan>`_ to test SSL/TLS enabled services to discover supported cipher suites
*   `crt.sh <https://crt.sh/>`_ to find SSL/TLS certificates issued for specific domains or organizations
*   `cyberzero PQC Edge Scanner <https://scan.cyberzero.io/>`_ to scan for PQC transition signals at the public edge of any domain
*   `Cisco Mercury <https://github.com/cisco/mercury/>`_ 
*   `CodeQL <https://docs.github.com/en/code-security/concepts/code-scanning/codeql/about-code-scanning-with-codeql>`_ 
*   `SonarQube Plugin that detects cryptographic assets in source code and generates CBOM <https://github.com/cbomkit/sonar-cryptography>`_
*   `A toolset for dealing with Cryptography Bill of Materials (CBOM) <https://github.com/cbomkit/cbomkit>`_
*   `Cryptographic asset discovery and PQC readiness scanner with CycloneDX CBOM output <https://github.com/CipherIQ/cbom-generator>`_

Commercial products are often described as Automated Discovery and Inventory tools. If you are aleady operating continuous diagnostics and monitoring tools in your enterprise, consider asking your current tool providers if their tool can be leveraged for disocvery and inventory of crytography algorithms in use, communication protocols and services that use cryptography, cryptographic keys, certificates and certificate chains, systems, applications, or components that depend on cryptography, data protected by cryptography, cryptographic libraries, cryptographic parameters such as key lengths and operational modes, hardware roots of trust such as hardware security modules (HSMs), TPMs, smart cards, and secure enclaves hosting keys or offloading operations, etc.