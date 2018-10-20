/* argv[0] - prog name 
   argv[1] - REF_DWN 
   argv[2] - REF_LAT 
   argv[3] - dist_DWN 
   argv[4] - dist_LAT
*/
/* retVal[0] = move_up
   retVal[1] = move_down
   retVal[2] = move_FWD
   retVal[3] = move_BWD
*/
#define REF_DWN argv[1]
#define DIST_DWN argv[2]
#define REF_FWD argv[3]
#define DIST_FWD argv[4]

unsigned char main(int argc, char* argv[])
{
	if(argc != 5u) return 0xFF;
	else
	{
		unsigned char retVal = 0;
		float diff_DWN = REF_DWN - DIST_DWN;
		float diff_FWD = REF_FWD - DIST_FWD;
		if(0 < diff_DWN)/* e mai jos decat trebuie */
		{
			retVal |= 0x01u; /* urca */
		}
		else if(0 > diff_DWN)
		{
			retVal |= (1u << 1u); /* coboara */
		}
		if(0 < diff_FWD)/* e mai aproape -> move BWD*/
		{
			retVal |= (1u << 3u);
		}
		else if(0 > diff_FWD)/* e mai departe -> move FWD*/
		{
			retVal |= (1u << 2u);
		}
		return retVal;
	}
}

