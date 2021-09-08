import time
import sys

if '--with-cython' in sys.argv or '-w' in sys.argv:
    import os
    os.system('python setup.py build_ext --inplace')
    from carre_cython import *
    start = time.time()
    print(main())
    print(time.time() - start)

else:

    from LPGCDM import *
    start = time.time()
    main()
    print(time.time() - start)