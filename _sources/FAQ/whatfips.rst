
What are Federal Information Processing Standards \(FIPS\)?
***********************

FIPS are standards for federal computer systems that are developed by \(NIST\) and approved by the Secretary of Commerce in accordance with the Information Technology Management Reform Act of 1996 and Computer Security Act of 1987.
These standards are developed when there are no acceptable industry standards or solutions for a particular government requirement.
Although FIPS are developed for use by the Federal Government, many in the private sector voluntarily use these standards.

What are the current FIPS?
----------------------------

The list of current FIPS—those that have been published, plus draft FIPS posted for comment—can be found on NIST's `Computer Security Resource Center \(CSRC\) <https://csrc.nist.gov/publications/fips>`_.

What are the Federal Information Processing Standards \(FIPS\) for PQC?
---------------------------------------------------------------------------

**There are currently three finalized Federal Information Processing Standards \(FIPS\) for Post-Quantum Cryptography:**

*   **FIPS 203:** `Module-Lattice-Based Key-Encapsulation Mechanism Standard <https://csrc.nist.gov/pubs/fips/203/final>`_
*   **FIPS 204:** `Module-Lattice-Based Digital Signature Standard <https://csrc.nist.gov/pubs/fips/204/final>`_
*   **FIPS 205:** `Stateless Hash-Based Digital Signature Standard <https://csrc.nist.gov/pubs/fips/205/final>`_

These standards specify key establishment and digital signature schemes that are designed to resist future attacks by quantum computers, which threaten the security of current standards.
The three algorithms specified in these standards are each derived from different submissions to the `NIST Post-Quantum Cryptography Standardization Project <https://csrc.nist.gov/Projects/post-quantum-cryptography>`_.   

Key Encapsulation Mechanism
++++++++++++++++++++++++++++++++++++++++++

FIPS 203 specifies a cryptographic scheme called the Module-Lattice-Based Key-Encapsulation Mechanism Standard, which is derived from the CRYSTALS-KYBER submission.
A key encapsulation mechanism \(KEM\) is a particular type of key establishment scheme that can be used to establish a shared secret key between two parties communicating over a public channel.

Current NIST-approved key establishment schemes are specified in NIST Special Publications \(SP\):  `SP 800-56A, Recommendation for Pair-Wise Key-Establishment Schemes Using Discrete Logarithm-Based Cryptography <https://csrc.nist.gov/pubs/sp/800/56/a/r3/final>`_, and `SP 800-56B, Recommendation for Pair-Wise Key-Establishment Schemes Using Integer Factorization Cryptography <https://csrc.nist.gov/pubs/sp/800/56/b/r2/final>`_. 

NIST has also chosen Hamming Quasi-Cyclic \(HQC\) to be standardized.
NIST will develop a standard based on HQC to augment its key-establishment portfolio.


Digital Signatures
++++++++++++++++++++++++++++++++++++++++++

FIPS 204 and 205 each specify digital signature schemes, which are used to detect unauthorized modifications to data and to authenticate the identity of the signatory. 
FIPS 204 specifies the Module-Lattice-Based Digital Signature Standard, which is derived from the CRYSTALS-Dilithium submission. 
FIPS 205 specifies the Stateless Hash-Based Digital Signature Standard, which is derived from the SPHINCS+ submission.

Current NIST-approved digital signature schemes are specified in `FIPS 186-5, Digital Signature Standard <https://csrc.nist.gov/pubs/fips/186-5/final>`_, and `SP 800-208, Recommendation for Stateful Hash-Based Signature Schemes <https://csrc.nist.gov/pubs/sp/800/208/final>`_.

NIST is also developing a FIPS that specifies a digital signature algorithm derived from FALCON as an additional alternative to these standards.

Does NIST have validation testing of approved \(i.e., FIPS-approved and NIST-recommended\) cryptographic algorithms and their individual components?
----------------------------------------------------------------------------------------------------------------------------------------------------

NIST's `Cryptographic Algorithm Validation Program \(CAVP\) <https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program>`_ offers two Automated Cryptographic Validation Test Systems \(ACVTS\) for interested users to test cryptographic algorithm implementations.
A Demo ACVTS server is available at no cost to interested parties. More information on accessing the ACVTS can be found the CAVP page on `Accessing the ACVTS <https://csrc.nist.gov/Projects/cryptographic-algorithm-validation-program/how-to-access-acvts>`_.

The Production ACVTS server is only available to National Voluntary Laboratory Accreditation Program \(NVLAP\) accredited testing laboratories, and is the only way to create algorithm validation certificates listed on the `Algorithm Validation Search Page <https://csrc.nist.gov/Projects/cryptographic-algorithm-validation-program/validation-search>`_.
The CAVP, through ACVTS, will generate test vectors to match the capabilities of a given implementation under test. The CAVP is not responsible for running those test vectors through the implementation. 

Example: `CAVP List of Validated PQC Algorithms <https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program/validation-search?searchMode=validation&productType=-1&algorithm=179&ipp=25>`_


Does NIST have a security metric to use in procuring equipment containing validated cryptographic modules?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NIST's `Cryptographic Module Validation Program \(CMVP\) <https://csrc.nist.gov/projects/cryptographic-module-validation-program>`_ aims to promote the use of validated cryptographic modules and provide Federal agencies with a security metric to use in procuring equipment containing validated cryptographic modules. 

Is there a way to use a suite of automated tools that would permit organizations to perform testing of their cryptographic products according to the requirements of FIPS 140-3, then directly report the results to NIST using appropriate protocols?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NIST's NCCoE has an `Automation of the NIST Cryptographic Module Validation Project <https://pages.nist.gov/ACMVPDocs/overview.html>`_.
