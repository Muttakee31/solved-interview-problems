class Solution {
public:
    string Count(string str) {
    string out;
    int same,flag;
    for (int i=0;i<str.length();i++) {
        same=0;
        for (int j=i;str[i]==str[j];j++) {
            same++;
        }
        stringstream ss;
        ss<<same;
        string temp = ss.str();
        out+=temp+str[i];
        i+=same-1;
        //cout<<"asdaf "<<i<<endl;
        }
    //cout<<out<<endl;
    return out;
}

    string countAndSay(int n) {
        string pat[300];
        pat[0]="1";
        Count(pat[0]);
        for (int i=1;i<=n;i++) {
            pat[i]=Count(pat[i-1]);
        }
        return pat[n-1];
    }
};