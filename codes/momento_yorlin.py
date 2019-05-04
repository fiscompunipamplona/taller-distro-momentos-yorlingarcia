class Momento: 

    m1 = 0.
    N = 0
    m21 = 0.
    m22 = 0.
    bins = []
    freqs = []
    m3 = 0.
    m4 = 0.

    def init(self):
        self.m1 = 0.
        self.N = 0

    def momento1(self, dfile):
        for i in dfile:
            column = i.split()
            if column[0] != "#":
                bin_i = float (column[0])
                freq = float (column[1])
                self.m1 += bin_i * freq
                self.N += freq
                self.bins.append(bin_i)
                self.freqs.append(freq)
        media = (self.m1)/(self.N)
        #print ( "cd: %0.4f, sd: %0.4f\n" % (self.N, self.m1))
        print ("media: %0.4f\n " % (media))
        dfile.close()
        return ([media, self.N])

    def momento2(self, media, N):
        for j in range(len(self.bins)):
            self.m21 += self.freqs[j]*abs(self.bins[j] - media)
            self.m22 += self.freqs[j]*(self.bins[j] - media)**2
        var = (1/(N-1))*self.m22
        sigma = var**0.5
        Adev = (1/N)*self.m21
        print ("varianza: %0.4f\n, desviacion estandar: %0.4f, desviacion absoluta: %0.4f\n" % (var, sigma, Adev))
        return(sigma)

    def momento3(self, media ,N, sigma):
        for k in range(len(self.bins)):
            self.m3 +=self.freqs[k]*((self.bins[k] - media)/sigma)**3
        skew = (1/N)*self.m3
        print ("grado de asimetria: %0.4f\n" % (skew))

    def momento4(self, media, N, sigma):
        for i in range(len(self.bins)):
            self.m4 += self.freqs[i]*((self.bins[i]-media)/sigma)**4
        kurt = ((1/N)*self.m4)-3
        print ("kurtosis: %0.4f\n" % (kurt))
