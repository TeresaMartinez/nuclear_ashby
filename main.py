import xs
import melting_point
import periodictable as pt
import pylab as pl

xs_list = (('Total Cross Section','tot'),
           ('Elastic Scattering Cross Section','ela'),
           ('Total Inelastic Cross Section','inl'),
           ('(n,2n) Cross Section','n2n'),
           ('(n,3n) Cross Section','n3n'),
           ('Total Fission Cross Section','fis'),
		   ('(n,4n) Cross Section','n4n'),
           ('(n,na) Cross Section','nna'),
           ('(n,np) Cross Section','nnp'),
           ('(n,nd) Cross Section','nnd'),
           ('Radiative Capture Cross Section','cap'),
           ('(n,p) Cross Section','n_p'),
           ('(n,d) Cross Section','n_d'),
           ('(n,t) Cross Section','n_t'),
           ('(n,alpha) Cross Section','n_a'))

xs_descr = [a[0] for a in xs_list]
xs_short = [a[1] for a in xs_list]

xs_nrg = (('at 0.0253 eV','thr', 0.),
          ('Maxwell avg. at 0.0253 eV','mxw', 0.),
          ('at 14 MeV','14M',0.),
          ('Fission spectrum avg.','fsp', 0.),
          ('Resonance integral', 'rin', 0.),
          ('g-factor','g_f', 1.))
nrg_descr = [a[0] for a in xs_nrg]
nrg_short = [a[1] for a in xs_nrg]
xs_default = [a[2] for a in xs_nrg]

tag = 0
nrg_tag = xs_nrg[tag][1]

D = []
for el in pt.elements:
	s_xs = 'pt.'+ el.symbol +'.xs.tot[\''+nrg_tag+'\'] - pt.' + el.symbol + '.xs.ela[\''+nrg_tag+'\'] - pt.' + el.symbol + '.xs.inl[\''+nrg_tag+'\']'
	s_mp = 'pt.'+ el.symbol + '.melting_point'
	if 'xs' in dir(el):
		if 'melting_point' in dir(el):
			D.append((eval(s_mp),eval(s_xs),el.symbol))
		
	# Accumulate data as a function of the atomic number
	# if 'xs' and 'melting_point' in dir(el):
	#	D.append((el.number,eval(s_xs),el.symbol))

params = {'figure.figsize': (10,8)}
# pl.rcParams.update(params)
bbox = dict(boxstyle="round",lw=0.5,ec=(0,0,0),fc=(0.85,0.8,0.8))
fs = 12

pl.semilogx()
for Z,XS,sym in D:
    if XS >= 1.e-4:
        pl.text(XS,Z,'{}'.format(sym),bbox=bbox,ha='center',va='center',fontsize=fs) # width=3.

xmin = min([D[i][0] for i in range(len(D))])
xmax = max([D[i][0] for i in range(len(D))])
ymin = min([D[i][1] for i in range(len(D))])
ymax = max([D[i][1] for i in range(len(D))])

# print xmin, xmax, ymin, ymax
pl.axis([1.e-4,1.e4,-500.,5000.])
pl.xlabel('Cross-section, cm$^{-1}$', fontsize=fs)
pl.ylabel('Melting point, $^\circ$C', fontsize=fs)
pl.title('Melting point vs. macroscopic absorption cross-section '+ xs_nrg[tag][0], fontsize=fs)
pl.tick_params(labelsize=fs, which='both')
pl.draw()
# pl.savefig('abs_'+xs_nrg[tag][1])
pl.savefig('abs_'+xs_nrg[tag][1], bbox_inches='tight', dpi=300)
pl.close()
