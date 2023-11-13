# rect(t/T)=1 [-0.5T,0.5T]
# Tsinc(fT),pole=1/T,amp=T
# tri(t/T) [-T,T]
# Tsinc^2(fT),pole=1/T,amp=T,abs

# Modulation and Demodulation
# fullAM(envelop
# |[A_0+m(t)]cos(w_c*t)
# DSBAM(cpherante
# |m(t)cos(w_c*t)
# PM(FMdemod->int(dt))
# |Acos[w_ct+Km(t)]
# FM(d/dt->envelop->DCblock->
# |Acos[w_ct+K*int{m(t)}]
# WBFM
# |As=*sig{J_n(beta)*cos[(w_c+n*w_m)*t]}
# digBassIdealchan(matchFilter->detector
# digBassReal
# |u*p(t)=g(t)**h(t)**c(t)
# |C(f)=[u*P(f)]/[G(f)*H(f)]
# FSK
# |g_k=cos(2pi()f_k*t), f_k=f_0,f_1
# PSK
# |g_k=cos(2pi()ft+phi(k)), phi(k)=0,pi()


# Carson's LAW
# |B_fm=2(beta+1)f_m
# |beta=df/f_m
# SNR
# AM
# |Ac^2/(4n*f_m)
# |n/2 psd_noise
# FM
# |(3beta^2*Ac^2)/(4n*f_m)

# fmDefine
# |delta[phi(t)]/k_p*m(t):instantaneous phase deviation
# |delta[f(t)]/k_f*m(t):Instantaneous carrier frequency deviation
# Match Filter
# |c(t)=kg(T-t)
# Threshold lambda
# |
# BER
# |P_eorr=p*p(|)+p*p(|)
# digBass
# |p_e=Q[sqar(2E_b/N_0)] (whenP=P=0.5)
# FSK
# |p_e=Q[sqar{(1-rho)E_b/N_0}]
# QPSK
# |p_e=Q[sqar(2E_b/N_0)]
