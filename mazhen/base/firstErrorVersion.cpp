// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

bool isBadVersion(int version){};

class Solution {
public:
    int firstBadVersion(int n) {
        int l=1,r=n,mid;
        while(l<r){
            mid=(long)l+r>>1;
            if(isBadVersion(mid)==true)  r=mid;
            else l=mid+1;
        }
        return l;
    }
};