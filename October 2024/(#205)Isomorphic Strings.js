var isIsomorphic = function (s, t) {
    res1 = {}
    res2 = {}

    if (s.length != t.length)
        return false;
    for (let i = 0; i < s.length; i++) {
        if (!res1[s[i]])
            res1[s[i]] = t[i];
        
        else {
            if (res1[s[i]] != t[i])
                return false;
            else
                continue;
        }

        if (!res2[t[i]])
            res2[t[i]] = s[i];
        else {
            if (res2[t[i]] != s[i])
                return false;
            else
                continue;
        }
    }
    
    return true;
};