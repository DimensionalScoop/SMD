  ////////////////////////////////////////////////////////////////////////////////
  ///  Machine independent random number generator.
  ///  Based on the BSD Unix (Rand) Linear congrential generator.
  ///  Produces uniformly-distributed floating points between 0 and 1.
  ///  Identical sequence on all machines of >= 32 bits.
  ///  Periodicity = 2**31, generates a number in (0,1).
  ///  Note that this is a generator which is known to have defects
  ///  (the lower random bits are correlated) and therefore should NOT be
  ///  used in any statistical study).

  Double_t TRandom::Rndm( )
  {
  #ifdef OLD_TRANDOM_IMPL
     const Double_t kCONS = 4.6566128730774E-10;
     const Int_t kMASK24  = 2147483392;

     fSeed *= 69069;
     UInt_t jy = (fSeed&kMASK24); // Set lower 8 bits to zero to assure exact float
     if (jy) return kCONS*jy;
     return Rndm();
  #endif

     // kCONS = 1./2147483648 = 1./(RAND_MAX+1) and RAND_MAX= 0x7fffffffUL
     const Double_t kCONS = 4.6566128730774E-10; // (1/pow(2,31)
     fSeed = (1103515245 * fSeed + 12345) & 0x7fffffffUL;

     if (fSeed) return  kCONS*fSeed;
     return Rndm();
  }
