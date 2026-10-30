
Which Federal Information Processing Standards \(FIPS\) are the ones for PQC?
*****************************************************************************

**There are three Federal Information Processing Standards \(FIPS\) for Post-Quantum Cryptography:**

*   **FIPS 203:** `Module-Lattice-Based Key-Encapsulation Mechanism Standard <https://csrc.nist.gov/pubs/fips/203/final>`_
*   **FIPS 204:** `Module-Lattice-Based Digital Signature Standard <https://csrc.nist.gov/pubs/fips/204/final>`_
*   **FIPS 205:** `Stateless Hash-Based Digital Signature Standard <https://csrc.nist.gov/pubs/fips/205/final>`_

These standards specify key establishment and digital signature schemes that are designed to resist future attacks by quantum computers, which threaten the security of current standards.
The three algorithms specified in these standards are each derived from different submissions to the `NIST Post-Quantum Cryptography Standardization Project <https://csrc.nist.gov/Projects/post-quantum-cryptography>`_.  This page offers opportunities to learn about quantum-resistent Key Encapsulation Mechanism algorithms and Digital Signature algorithms

Does NIST have validation testing of approved cryptographic algorithms and their individual components?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

NIST's `Cryptographic Algorithm Validation Program \(CAVP\) <https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program>`_ offers two Automated Cryptographic Validation Test Systems \(ACVTS\) for interested users to test cryptographic algorithm implementations.
A Demo ACVTS server is available at no cost to interested parties. More information on accessing the ACVTS can be found the CAVP page on `Accessing the ACVTS <https://csrc.nist.gov/Projects/cryptographic-algorithm-validation-program/how-to-access-acvts>`_.

The Production ACVTS server is only available to National Voluntary Laboratory Accreditation Program \(NVLAP\) accredited testing laboratories, and is the only way to create algorithm validation certificates listed on the `Algorithm Validation Search Page <https://csrc.nist.gov/Projects/cryptographic-algorithm-validation-program/validation-search>`_.
The CAVP, through ACVTS, will generate test vectors to match the capabilities of a given implementation under test. The CAVP is not responsible for running those test vectors through the implementation. 

Example: `CAVP List of Validated PQC Algorithms <https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program/validation-search?searchMode=validation&productType=-1&algorithm=179&ipp=25>`_


Does NIST have a security metric to use in procuring equipment containing validated cryptographic modules?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

NIST's `Cryptographic Module Validation Program \(CMVP\) <https://csrc.nist.gov/projects/cryptographic-module-validation-program>`_ promotes the use of validated cryptographic modules and provide Federal agencies with a security metric to use in procuring equipment containing validated cryptographic modules. 
