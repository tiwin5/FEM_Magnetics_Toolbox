Include "Parameter.pro";

Function{
  // Liste von Lukas hinterlegen
  // Mu_imag muss noch aus mur und


  // --------------------------
  // TDK N95 100 Celsius

  // --------------- 100 kHz ---- normalized on mur = 3000
  N95_b_100000 = {
  0.000000000000000000e+00, 1.022499999999999971e-02, 1.234999999999999987e-02, 1.326300000000000048e-02, 1.850900000000000115e-02, 1.339899999999999945e-02, 1.684499999999999886e-02, 1.713399999999999992e-02, 1.186199999999999928e-02, 7.047799999999999898e-03, 1.043600000000000083e-02, 1.421599999999999947e-02, 3.768699999999999828e-02, 4.533000000000000224e-02, 5.370199999999999974e-02, 5.684999999999999776e-02, 7.487399999999999611e-02, 7.514999999999999458e-02, 9.262399999999999800e-02, 1.032600000000000046e-01, 1.033300000000000052e-01, 1.056799999999999962e-01, 1.039599999999999969e-01, 1.040800000000000058e-01, 1.130199999999999955e-01, 1.170699999999999935e-01, 1.191799999999999943e-01, 1.202600000000000058e-01, 1.314700000000000035e-01, 1.274800000000000100e-01, 1.280900000000000094e-01, 1.328999999999999904e-01, 1.399199999999999888e-01, 1.443399999999999961e-01, 1.535600000000000021e-01, 1.616599999999999981e-01, 1.708000000000000074e-01, 1.738099999999999923e-01, 1.836299999999999877e-01, 1.921100000000000030e-01, 2.036799999999999999e-01, 2.077799999999999925e-01, 2.089100000000000124e-01, 2.170799999999999952e-01, 2.273050000000000070e-01, 2.294299999999999951e-01, 2.303429999999999922e-01, 2.355889999999999929e-01, 2.304789999999999894e-01, 2.339249999999999940e-01, 2.342140000000000055e-01, 2.289420000000000066e-01, 2.241277999999999881e-01, 2.275159999999999960e-01, 2.312960000000000016e-01, 2.547669999999999657e-01, 2.624099999999999766e-01, 2.707819999999999672e-01, 2.739300000000000068e-01, 2.919539999999999913e-01, 2.922299999999999898e-01, 3.097039999999999793e-01, 3.203400000000000136e-01, 3.204099999999999726e-01, 3.227599999999999913e-01, 3.210399999999999920e-01, 3.211600000000000010e-01, 3.301000000000000045e-01, 3.341500000000000026e-01, 3.362600000000000033e-01, 3.373399999999999732e-01, 3.485500000000000265e-01, 3.445599999999999774e-01, 3.451699999999999768e-01, 3.499799999999999578e-01, 3.569999999999999840e-01, 3.614199999999999635e-01, 3.706399999999999695e-01, 3.787399999999999656e-01, 3.878800000000000026e-01, 3.908899999999999597e-01, 4.007100000000000106e-01, 4.091899999999999982e-01, 4.207600000000000229e-01, 4.248600000000000154e-01, 4.259899999999999798e-01, 4.341599999999999904e-01
  } ;

  N95_mu_imag_100000 = {
  4.302477274611538505e+00, 1.574687606672626039e+01, 1.812527311166454425e+01, 1.914714099509493650e+01, 2.501863747635101731e+01, 1.929935771054042704e+01, 2.315624302165453940e+01, 2.347970041143049968e+01, 1.757908217911182192e+01, 1.219079072759320681e+01, 1.598303736981330303e+01, 2.021377618419723277e+01, 4.648230351050768405e+01, 5.503560723396976329e+01, 6.440422089794398630e+01, 6.792680523850738439e+01, 8.809355147431138278e+01, 8.840233452758775456e+01, 1.079498351534895733e+02, 1.198457315264572429e+02, 1.199240173902311852e+02, 1.225521378717725582e+02, 1.206285864770338065e+02, 1.207627893582183276e+02, 1.307602047170632034e+02, 1.352887630632850176e+02, 1.376479643257557939e+02, 1.388554846658810789e+02, 1.513877309559354671e+02, 1.469273930883821038e+02, 1.476093207083198990e+02, 1.529862170144977256e+02, 1.608326901998018741e+02, 1.657724996164931213e+02, 1.760753413561499485e+02, 1.851249297220809638e+02, 1.953344060914024567e+02, 1.986961164569628977e+02, 2.096617924034063662e+02, 2.191288747111781845e+02, 2.320420803653456119e+02, 2.366170399518569241e+02, 2.378778465783687182e+02, 2.469923183043913752e+02, 2.583961097469982633e+02, 2.607656243945216943e+02, 2.617836291420359771e+02, 2.676323828572901675e+02, 2.619352679976317404e+02, 2.657773029205710031e+02, 2.660994966502390753e+02, 2.602214867689797302e+02, 2.548530204556742831e+02, 2.586313959003551872e+02, 2.628462019151963887e+02, 2.890049988892925512e+02, 2.975185561697269350e+02, 3.068413696197637819e+02, 3.103461204580088975e+02, 3.304043227173619925e+02, 3.307113584554522845e+02, 3.501430039619047534e+02, 3.619633422511814160e+02, 3.620411182057606538e+02, 3.646520244795246981e+02, 3.627410906786994929e+02, 3.628744164978451749e+02, 3.728051260428995874e+02, 3.773025790255420588e+02, 3.796453558480167771e+02, 3.808444113398418835e+02, 3.932864755914924899e+02, 3.888587214916576613e+02, 3.895357023476266249e+02, 3.948731532694287694e+02, 4.026606594891264308e+02, 4.075624904972704599e+02, 4.177839941376350339e+02, 4.267597648948259348e+02, 4.368832959415505002e+02, 4.402160877925791169e+02, 4.510853006879528948e+02, 4.604664754152854584e+02, 4.732585736645123689e+02, 4.777895383607463486e+02, 4.790381203645362689e+02, 4.880629318493609503e+02
  } ;

  N95_mu_imag_couples_100000 = ListAlt[N95_b_100000(), N95_mu_imag_100000()] ;

  f_N95_mu_imag_100000[] = InterpolationLinear[Norm[$1]]{List[N95_mu_imag_couples_100000]};


  // --------------- 200 kHz ---- normalized on mur = 3000
  N95_b_200000 = {
  0.000000000000000000e+00, 2.144700000000000079e-02, 2.150099999999999928e-02, 2.132799999999999974e-02, 2.081399999999999917e-02, 2.086700000000000013e-02, 2.117199999999999985e-02, 2.058300000000000060e-02, 2.030399999999999913e-02, 2.091600000000000056e-02, 2.454999999999999891e-02, 2.633299999999999877e-02, 2.176700000000000162e-02, 2.197400000000000048e-02, 2.276900000000000104e-02, 2.588700000000000029e-02, 3.192699999999999705e-02, 3.809699999999999892e-02, 5.890000000000000097e-02, 6.658100000000000129e-02, 6.677299999999999902e-02, 6.954200000000000659e-02, 7.366899999999999837e-02, 7.554700000000000304e-02, 8.095199999999999618e-02, 8.383699999999999486e-02, 9.049300000000000399e-02, 9.800999999999999990e-02, 1.040399999999999936e-01, 1.079299999999999982e-01, 1.130000000000000032e-01, 1.181600000000000011e-01, 1.204199999999999993e-01, 1.280600000000000072e-01, 1.314700000000000035e-01, 1.353800000000000003e-01, 1.434100000000000097e-01, 1.474000000000000032e-01, 1.529500000000000026e-01, 1.625900000000000123e-01, 1.703099999999999892e-01, 1.792700000000000127e-01, 1.837499999999999967e-01, 1.886099999999999999e-01, 1.991999999999999882e-01, 2.076800000000000035e-01, 2.140799999999999925e-01, 2.187300000000000078e-01, 2.401770000000000016e-01, 2.402310000000000001e-01, 2.400579999999999936e-01, 2.395440000000000069e-01, 2.395970000000000044e-01, 2.399020000000000041e-01, 2.393129999999999979e-01, 2.390339999999999965e-01, 2.396459999999999979e-01, 2.432799999999999963e-01, 2.450630000000000031e-01, 2.404970000000000163e-01, 2.407040000000000013e-01, 2.414990000000000192e-01, 2.446170000000000011e-01, 2.506570000000000187e-01, 2.568270000000000275e-01, 2.776299999999999879e-01, 2.853109999999999813e-01, 2.855030000000000068e-01, 2.882720000000000282e-01, 2.923990000000000200e-01, 2.942770000000000108e-01, 2.996820000000000039e-01, 3.025670000000000304e-01, 3.092230000000000256e-01, 3.167400000000000215e-01, 3.227700000000000014e-01, 3.266600000000000059e-01, 3.317300000000000249e-01, 3.368900000000000228e-01, 3.391500000000000070e-01, 3.467900000000000427e-01, 3.502000000000000113e-01, 3.541100000000000358e-01, 3.621400000000000174e-01, 3.661300000000000110e-01, 3.716800000000000104e-01, 3.813199999999999923e-01, 3.890399999999999969e-01, 3.980000000000000204e-01, 4.024800000000000044e-01, 4.073400000000000354e-01, 4.179300000000000237e-01, 4.264100000000000112e-01, 4.328100000000000280e-01, 4.374600000000000155e-01
  } ;

  N95_mu_imag_200000 = {
  6.258888748789551215e+01, 1.252130146489693487e+02, 1.253706343760346442e+02, 1.248656662510211248e+02, 1.233653354794711419e+02, 1.235200402825443575e+02, 1.244103162321726330e+02, 1.226910522226929032e+02, 1.218766498848220436e+02, 1.236630689587122447e+02, 1.342697357040622705e+02, 1.394732255814030282e+02, 1.261470524077421942e+02, 1.267512515636827430e+02, 1.290716784920586804e+02, 1.381716623359328366e+02, 1.557958992450312223e+02, 1.737938961163604858e+02, 2.344265848365437819e+02, 2.567907284523421367e+02, 2.573495804091721197e+02, 2.654082632845560852e+02, 2.774155647769153461e+02, 2.828780407485270985e+02, 2.985940403024990815e+02, 3.069793329020024544e+02, 3.263157359629926191e+02, 3.481369114804107880e+02, 3.656280310361692614e+02, 3.769050365479272386e+02, 3.915946874835032645e+02, 4.065352980500567242e+02, 4.130758436576705321e+02, 4.351713604405687761e+02, 4.450256625771781387e+02, 4.563188311448487298e+02, 4.794907818348359569e+02, 4.909937999460491369e+02, 5.069818746610313269e+02, 5.347166795089017342e+02, 5.568936779849722143e+02, 5.825932376604441743e+02, 5.954265070856914690e+02, 6.093354896192479373e+02, 6.395956391417718123e+02, 6.637777301111806310e+02, 6.819984815071995854e+02, 6.952204209957068315e+02, 7.560146998405033401e+02, 7.561673646966717115e+02, 7.556782643523722527e+02, 7.542249726964629417e+02, 7.543748344710188576e+02, 7.552372075014391157e+02, 7.535717781098542218e+02, 7.527828039395366204e+02, 7.545133841352422905e+02, 7.647838699967616094e+02, 7.698195269904213092e+02, 7.569193499426881999e+02, 7.575045063314162235e+02, 7.597515597618071297e+02, 7.685601237414871321e+02, 7.856033087453421331e+02, 8.029852506758422805e+02, 8.613735615901614437e+02, 8.828439351757772329e+02, 8.833799968641749274e+02, 8.911075679842978161e+02, 9.026129280209664785e+02, 9.078436509254854627e+02, 9.228809886678320709e+02, 9.308969546031773916e+02, 9.493625000918116257e+02, 9.701686950016909350e+02, 9.868215200430422556e+02, 9.975463674222310146e+02, 1.011503000468684832e+03, 1.025682065410677524e+03, 1.031884141755516112e+03, 1.052813270083236148e+03, 1.062135933263834886e+03, 1.072811135600898979e+03, 1.094685947505485046e+03, 1.105530439936047060e+03, 1.120587094525696330e+03, 1.146661494338944976e+03, 1.167469897504951859e+03, 1.191537773538371312e+03, 1.203537808366537320e+03, 1.216529792319103990e+03, 1.244744713613551767e+03, 1.267242665648303273e+03, 1.284165113394403079e+03, 1.296429080553895346e+03
  } ;

  N95_mu_imag_couples_200000 = ListAlt[N95_b_200000(), N95_mu_imag_200000()] ;

  f_N95_mu_imag_200000[] = InterpolationLinear[Norm[$1]]{List[N95_mu_imag_couples_200000]};

  // --------------- 300 kHz ---- normalized on mur = 3000
  N95_b_300000 = {
  0.000000000000000000e+00, 1.517499999999999969e-03, 1.515099999999999910e-03, 1.516999999999999902e-03, 1.527900000000000005e-03, 1.538099999999999927e-03, 1.580900000000000100e-03, 1.636499999999999934e-03, 1.688000000000000047e-03, 3.352099999999999785e-03, 2.677899999999999985e-03, 3.111800000000000069e-03, 5.971999999999999878e-03, 1.860600000000000101e-02, 2.134799999999999892e-02, 2.415899999999999992e-02, 2.854999999999999899e-02, 3.081599999999999964e-02, 3.658600000000000046e-02, 4.192799999999999999e-02, 4.733400000000000107e-02, 5.818600000000000161e-02, 6.004700000000000315e-02, 6.273099999999999510e-02, 6.670900000000000440e-02, 6.927500000000000324e-02, 7.328199999999999992e-02, 7.641900000000000082e-02, 8.222899999999999654e-02, 8.432599999999999818e-02, 9.058599999999999985e-02, 1.029800000000000021e-01, 1.051799999999999957e-01, 1.063700000000000062e-01, 1.121499999999999997e-01, 1.173499999999999960e-01, 1.210999999999999993e-01, 1.248200000000000004e-01, 1.285300000000000054e-01, 1.319400000000000017e-01, 1.340600000000000125e-01, 1.440899999999999959e-01, 1.470700000000000063e-01, 1.523700000000000054e-01, 1.590600000000000069e-01, 1.590399999999999869e-01, 1.590300000000000047e-01, 1.629299999999999915e-01, 1.681400000000000117e-01, 1.724700000000000122e-01, 1.756800000000000028e-01, 1.786999999999999977e-01, 1.827699999999999880e-01, 1.869699999999999973e-01, 1.914700000000000013e-01, 1.937399999999999956e-01, 1.967399999999999982e-01, 1.993499999999999994e-01, 2.040200000000000069e-01, 2.078200000000000047e-01, 2.102799999999999947e-01, 2.118899999999999950e-01, 2.137900000000000078e-01, 2.168700000000000072e-01, 2.192900000000000127e-01, 2.208075000000000176e-01, 2.208051000000000041e-01, 2.208070000000000033e-01, 2.208179000000000114e-01, 2.208280999999999994e-01, 2.208709000000000089e-01, 2.209265000000000256e-01, 2.209780000000000078e-01, 2.226421000000000094e-01, 2.219679000000000235e-01, 2.224018000000000106e-01, 2.252620000000000178e-01, 2.378960000000000241e-01, 2.406380000000000186e-01, 2.434490000000000265e-01, 2.478400000000000047e-01, 2.501059999999999950e-01, 2.558759999999999923e-01, 2.612180000000000057e-01, 2.666240000000000276e-01, 2.774760000000000004e-01, 2.793370000000000020e-01, 2.820210000000000217e-01, 2.859990000000000032e-01, 2.885650000000000159e-01, 2.925719999999999987e-01, 2.957089999999999996e-01, 3.015189999999999815e-01, 3.036159999999999970e-01, 3.098760000000000403e-01, 3.222700000000000009e-01, 3.244700000000000362e-01, 3.256600000000000050e-01, 3.314400000000000124e-01, 3.366399999999999948e-01, 3.403900000000000259e-01, 3.441100000000000270e-01, 3.478200000000000180e-01, 3.512300000000000422e-01, 3.533500000000000529e-01, 3.633800000000000363e-01, 3.663600000000000190e-01, 3.716599999999999904e-01, 3.783500000000000196e-01, 3.783299999999999996e-01, 3.783199999999999896e-01, 3.822200000000000042e-01, 3.874300000000000521e-01, 3.917599999999999971e-01, 3.949700000000000433e-01, 3.979900000000000104e-01, 4.020599999999999730e-01, 4.062600000000000100e-01, 4.107600000000000140e-01, 4.130300000000000082e-01, 4.160300000000000109e-01, 4.186400000000000121e-01, 4.233100000000000196e-01, 4.271099999999999897e-01, 4.295700000000000074e-01, 4.311800000000000077e-01, 4.330800000000000205e-01, 4.361599999999999921e-01, 4.385800000000000254e-01
  } ;

  N95_mu_imag_300000 = {
  1.756181723408327571e+02, 1.845988549570703583e+02, 1.845846528605723336e+02, 1.845958961873089947e+02, 1.846603973272365238e+02, 1.847207561145141312e+02, 1.849740255014061745e+02, 1.853030370275024268e+02, 1.856077849164832401e+02, 1.954539355485504188e+02, 1.914650761892927449e+02, 1.940322560457522343e+02, 2.109510406047527908e+02, 2.855962480626757838e+02, 3.017748408644015399e+02, 3.183513507532803146e+02, 3.442252932381440473e+02, 3.575676682536443423e+02, 3.915088546509189200e+02, 4.228871077318218568e+02, 4.545932924262377242e+02, 5.180799774611962221e+02, 5.289441271447673216e+02, 5.446001494553167959e+02, 5.677758802947199683e+02, 5.827068054950420901e+02, 6.059924427689237518e+02, 6.241958549321407190e+02, 6.578462894455858532e+02, 6.699706530487112559e+02, 7.060952461485622962e+02, 7.772932272702646515e+02, 7.898837295369773983e+02, 7.966878393171297148e+02, 8.296730084051304175e+02, 8.592558647530803455e+02, 8.805335194280397673e+02, 9.015931738934341411e+02, 9.225476853439492970e+02, 9.417640486626880829e+02, 9.536893735427931915e+02, 1.009879183851150401e+03, 1.026498201581098101e+03, 1.055967179019429977e+03, 1.092999005401408112e+03, 1.092888578908889031e+03, 1.092833365022361932e+03, 1.114334191566044410e+03, 1.142953585569563529e+03, 1.166646925904136651e+03, 1.184156690635257746e+03, 1.200586557427497155e+03, 1.222661034581875811e+03, 1.245357646623511073e+03, 1.269580194462734653e+03, 1.281761143556090701e+03, 1.297819701234995364e+03, 1.311753557741957138e+03, 1.336597686963802971e+03, 1.356729555039318939e+03, 1.369721561877119029e+03, 1.378206952719550600e+03, 1.388202812710984972e+03, 1.404364985477600840e+03, 1.417027363670710201e+03, 1.424950996085899760e+03, 1.424938474575723831e+03, 1.424948387440589840e+03, 1.425005255592900085e+03, 1.425058471063131719e+03, 1.425281761037115984e+03, 1.425571814093363173e+03, 1.425840462990417109e+03, 1.434513248249285880e+03, 1.431001386296777582e+03, 1.433261833649434948e+03, 1.448135896378710640e+03, 1.513277196165095575e+03, 1.527291838157360189e+03, 1.541612587572355096e+03, 1.563887341143171170e+03, 1.575336389342155144e+03, 1.604346352116036314e+03, 1.631018560388125024e+03, 1.657825242462793994e+03, 1.711062700297024776e+03, 1.720113969454875587e+03, 1.733127022067173812e+03, 1.752324078369797462e+03, 1.764649710287094422e+03, 1.783806223001519811e+03, 1.798725467925586599e+03, 1.826174205027885364e+03, 1.836022320877448692e+03, 1.865232852126725675e+03, 1.922219596495109045e+03, 1.932215497868497778e+03, 1.937607162267353033e+03, 1.963642268429035539e+03, 1.986846013952806061e+03, 2.003449406480697235e+03, 2.019811257317006948e+03, 2.036020400610236720e+03, 2.050822319999777847e+03, 2.059977777880296799e+03, 2.102800540528867714e+03, 2.115365109045664667e+03, 2.137529932376849047e+03, 2.165172673812650373e+03, 2.165090596459965582e+03, 2.165049556515219138e+03, 2.180990835283756496e+03, 2.202084438434508684e+03, 2.219437668536123510e+03, 2.232197473951539905e+03, 2.244120022148601947e+03, 2.260061292785456772e+03, 2.276358436925364458e+03, 2.293645602102921202e+03, 2.302297268897693812e+03, 2.313660080870954971e+03, 2.323479586862361884e+03, 2.340894927303373152e+03, 2.354918804914269003e+03, 2.363926652175034178e+03, 2.369791796128449278e+03, 2.376682527743611899e+03, 2.387781535621375042e+03, 2.396440142755071065e+03
  } ;

  N95_mu_imag_couples_300000 = ListAlt[N95_b_300000(), N95_mu_imag_300000()] ;

  f_N95_mu_imag_300000[] = InterpolationLinear[Norm[$1]]{List[N95_mu_imag_couples_300000]};


  // -------------------------- ------------------------- --------------------------
  //f_N95_mu_imag[] = f_N95_mu_imag_200000[$1];
  //f_N95_mu_imag[] = f_N95_mu_imag_300000[$1];

  // frequency interpolation


  // Abfrage bei welcher Frequenz ->> Fallunterscheidung
  If(Freq<200000)
    f_N95_mu_imag[] = f_N95_mu_imag_100000[$1] + (f_N95_mu_imag_200000[$1] - f_N95_mu_imag_100000[$1]) / 100000 * ($2 - 100000);
  Else
    f_N95_mu_imag[] = f_N95_mu_imag_200000[$1] + (f_N95_mu_imag_300000[$1] - f_N95_mu_imag_200000[$1]) / 100000 * ($2 - 200000);
  EndIf
}