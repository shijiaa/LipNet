from setuptools import setup

setup(name='lipnet',
    version='0.1.6',
    description='End-to-end sentence-level lipreading',
    url='http://github.com/rizkiarm/LipNet',
    author='Muhammad Rizki A.R.M',
    author_email='rizki@rizkiarm.com',
    license='MIT',
    packages=['lipnet'],
    zip_safe=False,
	install_requires=[
        'Keras==2.2.4',
        'editdistance==0.5.3',
		'h5py==2.8.0',
		'matplotlib==3.0.3',
		'numpy==1.16.2',
		'scipy==1.2.1',
		'Pillow==4.3.0',
		'tensorflow-gpu==1.0.1',
		'Theano==1.0.4',
        'nltk==3.2.5',
        'sk-video==1.1.10',
        'dlib==19.16.0'
    ])
