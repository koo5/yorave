TRANSLATIONS=marave_es.ts\
             marave_he.ts\
             marave_de.ts\
             marave_pl.ts\
             marave_cs.ts\
             marave_it.ts\
             marave_el.ts\
             marave_fr.ts\
             marave_hu.ts

TRANSLATED=marave_es.qm\
           marave_he.qm\
           marave_de.qm\
           marave_pl.qm\
           marave_cs.qm\
           marave_hu.qm\
           marave_el.qm\
           marave_fr.qm\
           marave_it.qm

all: update_trans $(TRANSLATED)

marave_es.qm: marave_es.ts
	lrelease marave_es.ts -compress -qm marave_es.qm
marave_he.qm: marave_he.ts
	lrelease marave_he.ts -compress -qm marave_he.qm
marave_de.qm: marave_de.ts
	lrelease marave_de.ts -compress -qm marave_de.qm
marave_pl.qm: marave_pl.ts
	lrelease marave_pl.ts -compress -qm marave_pl.qm
marave_cs.qm: marave_cs.ts
	lrelease marave_cs.ts -compress -qm marave_cs.qm
marave_it.qm: marave_it.ts
	lrelease marave_it.ts -compress -qm marave_it.qm
marave_hu.qm: marave_hu.ts
	lrelease marave_hu.ts -compress -qm marave_hu.qm
marave_el.qm: marave_el.ts
	lrelease marave_el.ts -compress -qm marave_el.qm
marave_fr.qm: marave_fr.ts
	lrelease marave_fr.ts -compress -qm marave_fr.qm
	
update_trans:
	pylupdate4 ../*py ../editor/*py ../editor/widgets/*py -ts $(TRANSLATIONS)
	@for ts in ${TRANSLATIONS};\
	do \
	  sed 's/filename="/filename="..\//g' -i $$ts;\
	done

remove_obsolete:
	pylupdate4 -noobsolete ../*py -ts $(TRANSLATIONS)
	@for ts in ${TRANSLATIONS};\
	do \
	  sed 's/filename="/filename="..\//g' -i $$ts;\
	done
