"""NPLEX Part I Biomedical Science blueprint, as data.

Source: NABNE, NPLEX Part I Biomedical Sciences Study Guide (revised March 2026,
applies to August 2026 administrations).
https://www.nabne.org/pdf/NPLEX-Part-I-Biomedical-Sciences-Study-Guide-08-2026.pdf

Competency statements and condition lists follow the study guide. The following
are OUR additions, not NABNE's, and are marked as such in the output:
  - short names
  - default SEA tags per competency (NABNE does not assign SEAs to competencies)
  - nd: the naturopathic-emphasis flag (nutrition biochemistry, antioxidants,
    detoxification, exercise, deficiency states)
  - week / reinforce: course placement from the Master Blueprint Scaffold

SEA codes: A Anatomy, P Physiology, B Biochemistry & Genetics,
           M Microbiology & Immunology, X Pathology
"""

EXAM = {
    "items": 200, "sessions": 2, "perSession": 100, "minutesPerSession": 150,
    "clusters": 50, "perCluster": 4, "options": 4,
    "clusterFormat": "Each case opens with a brief summary that includes the patient's diagnosis, followed by four single-best-answer questions on its biomedical science.",
    "passRule": "A minimum score is required in BOTH general exam areas. Failing either one means retaking the whole exam.",
}

GEAS = [
    {"code": "SF", "name": "Structure/Function", "pct": 60, "seas": ["A", "P", "B"]},
    {"code": "DD", "name": "Disease/Dysfunction", "pct": 40, "seas": ["M", "X"]},
]

SEAS = [
    {"code": "A", "name": "Anatomy", "gea": "SF", "items": 40},
    {"code": "P", "name": "Physiology", "gea": "SF", "items": 40},
    {"code": "B", "name": "Biochemistry & Genetics", "gea": "SF", "items": 40},
    {"code": "M", "name": "Microbiology & Immunology", "gea": "DD", "items": 40},
    {"code": "X", "name": "Pathology", "gea": "DD", "items": 40},
]

# Shared statement templates (verbatim from the study guide, with the system phrase filled in)
BIOCHEM = "Explain biochemistry of proteins, carbohydrates, lipids, vitamins, minerals, and co-factors as they relate to {} function and pathology."
GENE = "Describe features and explain principles of gene expression, control, cell cycle regulation, and consequences of genetic abnormalities underlying {} disease."
IMMUNE = "Describe activation of innate and adaptive immune mechanisms by microbial pathogens, cancer/tumors, antigens, and vaccines; describe inflammatory, autoimmune, and hypersensitivity immune responses."
MICROBE = "Explain morphology, replication/life cycle, transmission (including vectors), mechanisms of infection, virulence factors, and genetic characteristics of common microbial pathogens causing listed conditions."
PATHO = "Explain pathogenesis and identify etiology, risk factors, complications, and clinical characteristics of the listed conditions."

# Each item: (number, short name, SEA codes, nd flag, statement)
SYSTEMS = [
  {"code": "CV", "name": "Cardiovascular", "full": "Cardiovascular System", "weight": 12, "week": 1, "reinforce": 3,
   "items": [
    (1, "Cardiovascular embryology", "A", 0, "Describe embryological development of the cardiovascular system, including valves, chambers, and blood vessels."),
    (2, "Heart and vessel histology", "A", 0, "Describe microscopic anatomy of the heart and blood vessels."),
    (3, "Heart, great vessels, and pericardium", "A", 0, "Describe location, structure, and boundaries of the heart, major vessels, and pericardium."),
    (4, "Heart valves and the cardiac cycle", "AP", 0, "Describe location and explain heart valve function in relation to the cardiac cycle."),
    (5, "Cardiac muscle contraction", "P", 0, "Explain physiological basis of contraction in cardiac muscle."),
    (6, "Cardiac cycle and its regulation", "P", 0, "Explain functions and regulatory mechanisms of the cardiac cycle."),
    (7, "Conduction system and the ECG", "AP", 0, "Describe location, function, autonomic regulation, and electrical measurement of the conduction system."),
    (8, "Coronary circulation", "A", 0, "Describe location and branching patterns of coronary arteries and circulatory pathways of blood supply."),
    (9, "Blood distribution to body regions", "A", 0, "Describe anatomical patterns of blood distribution to somatic and visceral areas."),
    (10, "Lymphatic vessels, tissues, and organs", "AP", 0, "Describe location, structure, circulatory pathways, and functions of lymphatic vessels, tissues, and organs."),
    (11, "Hemodynamics and blood flow regulation", "P", 0, "Describe forces involved in circulation of blood and lymph, and regulation of blood flow."),
    (12, "Exercise and the cardiovascular system", "P", 1, "Explain acute and adaptive effects of exercise on the cardiovascular system."),
    (13, "Cardiovascular biochemistry and nutrition", "B", 1, BIOCHEM.format("cardiovascular")),
    (14, "Cardiovascular genetics", "B", 0, GENE.format("cardiovascular")),
    (15, "Heart and lung interactions", "P", 0, "Explain relationship between cardiovascular and pulmonary systems."),
    (16, "Immune responses in cardiovascular disease", "M", 0, IMMUNE),
    (17, "Cardiovascular pathogens", "M", 0, MICROBE),
   ],
   "condNum": 18,
   "categories": [
    ("A", "Hypertensive heart diseases", ["Pulmonary hypertension", "Systemic hypertension"]),
    ("B", "Congestive heart failure", ["Left-sided", "Right-sided"]),
    ("C", "Ischemic heart disease", ["Angina pectoris", "Chronic ischemic heart disease", "Myocardial infarction (MI)"]),
    ("D", "Valvular heart diseases", ["Aortic stenosis/insufficiency", "Mitral stenosis/insufficiency", "Endocarditis", "Mitral valve prolapse (MVP)", "Rheumatic heart disease", "Carcinoid heart disease"]),
    ("E", "Primary myocardial diseases", ["Cardiomyopathies (dilated, restrictive, hypertrophic)", "Myocarditis"]),
    ("F", "Pericardial disease", ["Metastatic disease", "Pericardial effusions", "Pericarditis (primary and secondary)"]),
    ("G", "Congenital heart conditions", ["Bicuspid aortic valve", "Patent ductus arteriosus", "Septal defects (interventricular, atrial)", "Tetralogy of Fallot"]),
    ("H", "Hemodynamic conditions", ["Embolism", "Hemorrhage", "Infarction", "Edema", "Shock", "Thrombosis"]),
    ("I", "Vascular conditions", ["Aneurysm", "Aortic dissection", "Arteriosclerosis and atherosclerosis", "Familial hypercholesterolemia", "Giant cell arteritis (temporal arteritis)", "Peripheral arterial disease (PAD)", "Pulmonary embolism (PE)", "Raynaud phenomenon (primary and secondary)", "Thromboangiitis obliterans", "Thrombosis, deep vein (DVT)", "Varicose veins", "Vasculitis"]),
    ("J", "Vascular neoplasms", ["Hemangiomas", "Kaposi sarcoma"]),
    ("K", "Infectious vascular diseases", ["Bacterial endocarditis", "Chagas disease", "Lyme disease", "Rocky Mountain spotted fever", "Viral hemorrhagic fever (yellow fever, Dengue fever, filoviruses)", "Viral myocarditis"]),
   ]},

  {"code": "GI", "name": "Gastrointestinal", "full": "Gastrointestinal System", "weight": 12, "week": 2, "reinforce": 4,
   "items": [
    (1, "Gastrointestinal embryology", "A", 0, "Describe embryological development of the gastrointestinal tract and glands."),
    (2, "Gastrointestinal histology", "A", 0, "Describe microscopic anatomy of the gastrointestinal tract and glands."),
    (3, "Gastrointestinal organs and glands", "A", 0, "Describe location, structure, and boundaries of organs and glands of the gastrointestinal system."),
    (4, "The gut in the body cavities", "A", 0, "Describe gastrointestinal system in relation to oral, mediastinal, and abdominopelvic cavities."),
    (5, "Gastrointestinal blood supply", "A", 0, "Describe location, structure, and circulatory pathways of blood supply of the gastrointestinal system."),
    (6, "Motility, digestion, and absorption", "P", 0, "Explain mechanisms, functions, regulation, and factors affecting mastication, deglutition, digestion, absorption, peristalsis, and defecation."),
    (7, "Products of digestion", "P", 0, "Explain composition, function, transport, and regulation of products of digestion."),
    (8, "Digestive biochemistry and dietary requirements", "B", 1, "Explain biochemistry of digestive processes, including endogenous production of chemical energy and chemical composition and dietary requirements of proteins, carbohydrates, lipids, vitamins, minerals, and co-factors."),
    (9, "Liver detoxification, bilirubin, and gland functions", "BP", 1, "Explain non-digestive functions of salivary glands, liver, and gallbladder, including bilirubin metabolism and detoxification pathways."),
    (10, "Gastrointestinal genetics", "B", 0, GENE.format("gastrointestinal")),
    (11, "Immune responses in gastrointestinal disease", "M", 0, IMMUNE),
    (12, "Gastrointestinal pathogens", "M", 0, MICROBE),
   ],
   "condNum": 13,
   "categories": [
    ("A", "Salivary gland disease", ["Parotitis"]),
    ("B", "Pancreatic disease", ["Pancreatitis"]),
    ("C", "Hepatic diseases and disorders", ["Cholestasis", "Cirrhosis", "Gilbert syndrome", "Hepatitis (non-infectious)", "Portal hypertension"]),
    ("D", "Gallbladder diseases", ["Cholecystitis", "Cholelithiasis"]),
    ("E", "Deficiency and malabsorption conditions", ["Achlorhydria", "Gluten-sensitive enteropathy (celiac disease)", "Enzyme deficiencies", "Lactase deficiency"]),
    ("F", "Obstructive gastrointestinal diseases", ["Achalasia", "Adynamic ileus", "Hernia", "Intussusception/volvulus", "Megacolon"]),
    ("G", "Inflammatory gastrointestinal diseases", ["Appendicitis", "Barrett esophagus", "Diverticular disease", "Enteritis", "Esophageal/gastric/duodenal ulcers", "Esophagitis (non-infectious)", "Gastritis", "Gastroesophageal reflux disease (GERD)", "Inflammatory bowel disease (Crohn disease, ulcerative colitis)"]),
    ("H", "Congenital gastrointestinal disease", ["Esophageal atresia", "Esophageal webs and rings", "Meckel diverticulum", "Pyloric stenosis"]),
    ("I", "Conditions of the abdominal cavity", ["Ascites", "Peritonitis/adhesions"]),
    ("J", "Gastrointestinal vascular diseases", ["Esophageal varices", "Hemorrhoids", "Infarction", "Vascular ectasias of the colon"]),
    ("K", "Gastrointestinal neoplasms", ["Esophageal", "Gastric", "Intestinal (gastrinoma)", "Liver", "Oral (leukoplakia)", "Pancreas", "Colorectal"]),
    ("L", "Infectious gastrointestinal diseases", ["Enterocolitis", "Esophagitis", "Gastroenteritis", "Gingivitis/periodontitis", "Oral thrush", "Stomatitis", "Viral hepatitis"]),
   ]},

  {"code": "MS", "name": "Musculoskeletal", "full": "Musculoskeletal System", "weight": 10, "week": 3, "reinforce": 5,
   "items": [
    (1, "Musculoskeletal embryology", "A", 0, "Describe embryological development of the musculoskeletal system, including muscle, bone, and joints."),
    (2, "Muscle, bone, and joint histology", "A", 0, "Describe microscopic anatomy of the musculoskeletal system, including skeletal, cardiac, and smooth muscle; compact and spongy bone; and fibrous, cartilaginous, and synovial joints."),
    (3, "Axial and appendicular skeleton", "A", 0, "Describe location and structure, and explain function of vertebrae, skull bones, vertebral column, pectoral girdle, upper extremity, pelvic girdle, and lower extremity."),
    (4, "Joints: structure, innervation, and function", "AP", 0, "Describe location, structure, and innervation of joints, and explain functions of different joint types."),
    (5, "Muscles: origin, insertion, action, innervation", "A", 0, "Describe origin, insertion, main action, and innervation of muscles in body regions: head and neck; upper and lower extremities; back, thorax, abdomen, and pelvis."),
    (6, "Musculoskeletal connective tissue", "A", 0, "Describe embryology and structure, and explain function of connective tissues of the musculoskeletal system."),
    (7, "Muscle contraction", "P", 0, "Explain mechanisms and factors affecting contraction of skeletal, smooth, and cardiac muscle."),
    (8, "Musculoskeletal biochemistry and nutrition", "B", 1, BIOCHEM.format("musculoskeletal")),
    (9, "Musculoskeletal genetics", "B", 0, "Describe features and explain principles of gene expression, control, cell cycle regulation, and consequences of genetic defects underlying musculoskeletal disease."),
    (10, "Muscle and nerve interactions", "P", 0, "Explain relationship between musculoskeletal and neurological systems."),
    (11, "Immune responses in musculoskeletal disease", "M", 0, IMMUNE),
    (12, "Musculoskeletal pathogens", "M", 0, MICROBE),
   ],
   "condNum": 13,
   "categories": [
    ("A", "Musculoskeletal nutritional deficiencies", ["Osteomalacia", "Rickets", "Scurvy"]),
    ("B", "Inflammatory musculoskeletal diseases", ["Ankylosing spondylitis", "Bursitis", "Fibromyalgia", "Gout", "Myositis (dermatomyositis, polymyositis)", "Polymyalgia rheumatica (PMR)", "Reactive arthritis (Reiter syndrome)", "Tendonopathy"]),
    ("C", "Metabolic musculoskeletal diseases", ["Osteopetrosis"]),
    ("D", "Congenital musculoskeletal diseases", ["Marfan syndrome", "Muscular dystrophy", "Osteogenesis imperfecta"]),
    ("E", "Degenerative musculoskeletal diseases", ["Osteoarthritis (OA)/degenerative joint disease (DJD)", "Osteoporosis", "Paget disease", "Avascular necrosis"]),
    ("F", "Musculoskeletal neoplasms", ["Chondrosarcoma", "Ewing sarcoma", "Osteoid osteoma", "Osteosarcoma", "Rhabdomyosarcoma"]),
    ("G", "Infectious musculoskeletal diseases", ["Septic (infectious) arthritis", "Necrotizing fasciitis", "Osteomyelitis", "Wet and gas gangrene"]),
    ("H", "Trauma", ["Injury to the musculoskeletal system"]),
   ]},

  {"code": "NE", "name": "Neurological", "full": "Neurological System", "weight": 10, "week": 4, "reinforce": 6,
   "items": [
    (1, "Neural tube embryology", "A", 0, "Describe embryological development of the neural tube and derivatives."),
    (2, "Neuron and nerve histology", "A", 0, "Describe microscopic anatomy of motor and sensory neurons and nerves."),
    (3, "Brain and spinal cord structures", "AP", 0, "Describe location and structure, and explain function of neural structures in cranial cavity and vertebral canal."),
    (4, "Cerebrospinal fluid compartments and meninges", "AP", 0, "Describe location and structure, and explain function of cerebrospinal fluid compartments and meninges."),
    (5, "Sensory receptors, pathways, and reflexes", "AP", 0, "Describe location and explain functions of sensory receptors and associated anatomical pathways for somatic and visceral sensory perception and reflexes."),
    (6, "Special senses", "AP", 0, "Describe location, structure, pathways, and explain functions of special senses (visual, auditory, gustatory, olfactory, vestibular) and associated glands."),
    (7, "Somatic and visceral motor and sensory components", "AP", 0, "Describe location, pathways, functions of somatic motor and sensory components and visceral motor and sensory components."),
    (8, "Cranial and spinal nerves", "A", 0, "Describe location and explain function of cranial and spinal nerves."),
    (9, "Autonomic nervous system", "AP", 0, "Describe location and pathways, and explain functions of autonomic nervous system."),
    (10, "CNS blood supply and CSF flow", "A", 0, "Describe pathways of blood supply and origin and flow of cerebrospinal fluid for central nervous system."),
    (11, "Association cortex", "P", 0, "Describe pathways and explain functions and patterns of activity for association cortex."),
    (12, "Hypothalamic and limbic function", "P", 0, "Explain mechanisms, factors affecting, function, and control of hypothalamic and limbic pathways."),
    (13, "Synaptic transmission and action potentials", "P", 0, "Explain mechanisms, factors affecting, function, and control of synaptic transmission, graded potentials, action potential, and axon conduction."),
    (14, "Neurological biochemistry and nutrition", "B", 1, BIOCHEM.format("neurological")),
    (15, "Neurotransmitter synthesis and breakdown", "B", 0, "Explain biochemistry of neurotransmitter synthesis, function, and degradation."),
    (16, "Neurogenetics", "B", 0, GENE.format("neurological")),
    (17, "Nervous and endocrine system interactions", "P", 0, "Explain relationship of neurological system to endocrine system."),
    (18, "Immune responses in neurological disease", "M", 0, IMMUNE),
    (19, "Neurological pathogens", "M", 0, MICROBE),
   ],
   "condNum": 20,
   "categories": [
    ("A", "Neurological vascular disease", ["Cerebral infarction (thrombosis, embolism, common obstructions)", "Cerebral vascular accident (CVA) (ischemic/hemorrhagic)", "Ischemic-hypoxic encephalopathy", "Intracranial hemorrhage (cerebral, subarachnoid, epidural/subdural)", "Vascular lesions of spinal cord"]),
    ("B", "Degenerative and demyelination diseases", ["Alzheimer disease", "Amyotrophic lateral sclerosis (ALS)", "Extrapyramidal diseases (spinocerebellar degeneration, Huntington chorea, Parkinsonism)", "Guillain-Barré syndrome", "Multiple sclerosis (MS)", "Acute disseminated encephalomyelitis"]),
    ("C", "Diseases of increased intracranial fluid", ["Cerebral edema", "Hydrocephalus"]),
    ("D", "Metabolic and nutritional neurological diseases", ["Hepatic encephalopathy", "Peripheral neuropathy", "Vitamin B12 deficiency", "Wernicke-Korsakoff syndrome"]),
    ("E", "Congenital and genetic neurological diseases", ["Down syndrome", "Leukodystrophies", "Phenylketonuria (PKU)", "Storage diseases", "Wilson disease"]),
    ("F", "Neurological neoplasms", ["Medulloblastoma", "Meningiomas", "Neuroblastoma", "Neuroglial tumors (astrocytomas, oligodendrogliomas)", "Neuronal tumors", "Tumors of peripheral nerves (schwannoma, neurofibromatosis)"]),
    ("G", "Infections of the CNS and PNS", ["Arboviruses", "Botulism", "Brain abscess", "Encephalitis", "Fungal infections", "Herpes viruses", "Leprosy", "Meningitis", "Neurosyphilis", "Poliomyelitis", "Prion disease", "Progressive multifocal leukoencephalopathy (PML)", "Subacute sclerosing panencephalitis (SSPE)", "Tetanus", "Varicella zoster virus (VZV)"]),
    ("H", "CNS trauma", ["Traumatic brain injury (TBI) (concussion, contusion, hemorrhage, hematoma)", "Spinal cord compression/transection"]),
    ("I", "PNS trauma and compression", ["Bell palsy", "Carpal tunnel syndrome (CTS)", "Disc herniation", "Nerve root entrapment", "Sciatica", "Thoracic outlet syndrome (TOS)", "Trigeminal neuralgia"]),
    ("J", "Diseases of the special senses", ["Blepharitis", "Cataracts", "Conjunctivitis", "Glaucoma", "Iritis/keratitis", "Macular degeneration", "Uveitis", "Ménière disease (idiopathic endolymphatic hydrops)", "Otitis", "Vestibular neuritis and labyrinthitis"]),
   ]},

  {"code": "RE", "name": "Reproductive", "full": "Reproductive System", "weight": 10, "week": 5, "reinforce": 7,
   "items": [
    (1, "Reproductive, placental, and breast embryology", "A", 0, "Describe embryological development of male and female reproductive organs, placenta, and breast."),
    (2, "Reproductive gross and microscopic anatomy", "A", 0, "Describe gross and microscopic anatomy of male and female reproductive organs and breast."),
    (3, "Gametogenesis, implantation, and embryogenesis", "AP", 0, "Explain developmental processes related to gametogenesis, implantation, and embryogenesis."),
    (4, "Reproductive organ location and boundaries", "A", 0, "Describe location, structure, and boundaries of male and female reproductive systems and breast."),
    (5, "Reproductive innervation and blood supply", "A", 0, "Describe innervation and pathway of blood supply in reproductive organs and breast."),
    (6, "Reproductive processes and lactation", "P", 0, "Explain mechanisms, function, regulation, and factors affecting reproductive processes and lactation."),
    (7, "Reproductive hormones", "P", 0, "Explain composition, function, effects, transport, and regulation of reproductive hormones."),
    (8, "Reproductive hormone biochemistry", "B", 0, "Explain biochemistry of synthesis and degradation of hormones and other secretions involved in reproductive function and pathology."),
    (9, "Reproductive biochemistry and nutrition", "B", 1, BIOCHEM.format("reproductive")),
    (10, "Reproductive genetics", "B", 0, GENE.format("reproductive")),
    (11, "Immune responses in reproductive disease", "M", 0, IMMUNE),
    (12, "Reproductive pathogens", "M", 0, MICROBE),
   ],
   "condNum": 13,
   "categories": [
    ("A", "Reproductive hormone (endocrine) conditions", ["Amenorrhea", "Anovulation", "Dysfunctional uterine bleeding", "Menopause/perimenopause", "Ovarian insufficiency/failure"]),
    ("B", "Inflammatory diseases of the reproductive tract", ["Balanitis", "Cervicitis", "Endometriosis", "Endometritis", "Orchitis", "Pelvic inflammatory disease", "Salpingitis", "Vaginitis (candidal)"]),
    ("C", "Congenital and genetic reproductive diseases", ["Cryptorchidism", "Epispadias", "Fragile X syndrome", "Hypospadias", "Imperforate hymen", "Klinefelter syndrome", "Paraphimosis", "Phimosis", "Pseudohermaphroditism", "Septate vagina and uterus", "Turner syndrome"]),
    ("D", "Benign conditions of the penis and scrotum", ["Erectile dysfunction", "Hematocele", "Hydrocele", "Spermatocele", "Varicocele"]),
    ("E", "Conditions of the breast", ["Diffuse cystic mastopathy (fibrocystic breast disease)", "Galactocele", "Mammary duct ectasia", "Mastitis", "Traumatic fat necrosis", "Benign and malignant neoplasms (fibroadenoma, lobular carcinoma, ductal carcinoma, Paget disease of the breast)"]),
    ("F", "Infectious diseases and hyperplasia of the prostate", ["Benign prostatic hyperplasia", "Prostatitis"]),
    ("G", "Conditions of the ovary", ["Ovarian cysts", "Paraovarian cysts", "Polycystic ovary syndrome (PCOS)", "Tubo-ovarian cysts"]),
    ("H", "Diseases of the placenta", ["Choriocarcinoma", "Hydatidiform mole", "Invasive mole", "Preeclampsia"]),
    ("I", "Benign conditions of the vagina and vulva", ["Bartholin cysts", "Cystocele", "Rectocele", "Urethrocele"]),
    ("J", "Reproductive dysplasia and neoplasms", ["Cervical intraepithelial neoplasia (CIN)", "Endometrial hyperplasia", "Fibroids (leiomyoma)", "Invasive carcinoma of cervix", "Leiomyosarcomas", "Prostate carcinoma", "Tumors of ovary", "Squamous cell carcinoma of penis", "Testicular tumors", "Vaginal carcinoma", "Vulvar carcinoma", "Vulvar intraepithelial neoplasia"]),
    ("K", "Infectious diseases of the genitourinary system (including STDs)", ["Chancroid", "Bacterial vaginosis (BV)", "Chlamydia", "Gonorrhea", "Herpes simplex virus (HSV)", "Human papillomavirus (HPV)", "Nongonococcal urethritis", "Syphilis", "Toxic shock syndrome (TSS)", "Trichomoniasis"]),
   ]},

  {"code": "UR", "name": "Urinary", "full": "Urinary System", "weight": 10, "week": 6, "reinforce": 8,
   "items": [
    (1, "Urinary embryology", "A", 0, "Describe embryological development of urinary system organs."),
    (2, "Urinary histology", "A", 0, "Describe microscopic anatomy of urinary tract."),
    (3, "Urinary organs: location and boundaries", "A", 0, "Describe location, structure, and boundaries of urinary system."),
    (4, "Urinary system in the abdominopelvic cavity", "A", 0, "Describe location, structure, and boundaries of abdominopelvic cavity in relation to urinary system."),
    (5, "Renal circulation", "AP", 0, "Describe circulation of blood in urinary system."),
    (6, "Filtration, reabsorption, secretion, and micturition", "P", 0, "Explain mechanisms, functions, regulation of, and factors affecting micturition and urinary filtration, reabsorption, and secretion."),
    (7, "Kidney in acid-base and blood pressure control", "P", 0, "Describe role of kidney in acid-base balance and regulation of blood pressure."),
    (8, "Urinary biochemistry and nutrition", "B", 1, BIOCHEM.format("urinary")),
    (9, "Urinary genetics", "B", 0, GENE.format("urinary")),
    (10, "Immune responses in urinary disease", "M", 0, IMMUNE),
    (11, "Urinary pathogens", "M", 0, MICROBE),
   ],
   "condNum": 12,
   "categories": [
    ("A", "Glomerular diseases", ["Glomerulonephritis", "Glomerulosclerosis", "Nephrotic syndromes", "Renal failure (acute and chronic)"]),
    ("B", "Tubulointerstitial disease", ["Tubular necrosis"]),
    ("C", "Obstructive urinary diseases", ["Hydronephrosis", "Renal calculi"]),
    ("D", "Inflammatory urinary tract diseases", ["Drug-induced nephritis", "Chronic pyelonephritis"]),
    ("E", "Congenital urinary disease", ["Alport syndrome", "Cystic renal disease", "Renal agenesis", "Vesicoureteral reflux (VUR)"]),
    ("F", "Urinary vascular diseases", ["Hemolytic uremic syndrome (HUS)", "Hypertensive nephrosclerosis", "Renal artery stenosis", "Renal infarction", "Sickle cell nephropathy"]),
    ("G", "Neoplasms of the urinary tract", ["Renal cell carcinoma", "Nephroblastoma (Wilms tumor)"]),
    ("H", "Infectious urinary diseases", ["Acute pyelonephritis", "Cystitis", "Urethritis"]),
   ]},

  {"code": "EN", "name": "Endocrine", "full": "Endocrine System", "weight": 8, "week": 7, "reinforce": 9,
   "items": [
    (1, "Endocrine embryology", "A", 0, "Describe embryological development of endocrine system organs."),
    (2, "Endocrine histology and derivations", "A", 0, "Describe microscopic anatomy and derivations of endocrine organs."),
    (3, "Endocrine organ location and structure", "A", 0, "Describe location and structure of endocrine organs."),
    (4, "Endocrine blood supply", "A", 0, "Describe location, structure, and circulatory pathways of blood to endocrine organs."),
    (5, "Endocrine organ function and control", "P", 0, "Explain mechanisms, factors affecting, functions, and control of endocrine organs."),
    (6, "Hormone action, transport, and feedback", "P", 0, "Explain composition, function, effects, transport, and regulation of endocrine hormones, including feedback mechanisms."),
    (7, "Endocrine biochemistry and nutrition", "B", 1, BIOCHEM.format("endocrine")),
    (8, "Hormone synthesis and degradation", "B", 0, "Explain biochemistry of synthesis and degradation of hormones in the endocrine system."),
    (9, "Endocrine genetics", "B", 0, GENE.format("endocrine")),
    (10, "Immune responses in endocrine disease", "M", 0, IMMUNE),
    (11, "Endocrine pathogens", "M", 0, MICROBE),
   ],
   "condNum": 12,
   "categories": [
    ("A", "Diseases of endocrine hyperfunction", ["Hyperadrenalism (Cushing syndrome, Conn syndrome, congenital adrenal hyperplasia)", "Hyperparathyroidism (primary and secondary)", "Hyperpituitarism (acromegaly, gigantism)", "Hyperthyroidism (multinodular goiter, Graves disease)"]),
    ("B", "Diseases of endocrine hypofunction", ["Diabetes insipidus", "Hypoadrenalism (Addison disease, primary acute insufficiency, secondary adrenocortical insufficiency)", "Hypoparathyroidism", "Hypopituitarism (empty sella syndrome, hypothalamic lesions)", "Hypothyroidism (iodine deficiency goiter)"]),
    ("C", "Inflammatory endocrine diseases", ["Hashimoto thyroiditis", "Granulomatous subacute thyroiditis"]),
    ("D", "Metabolic endocrine disease", ["Diabetes types 1 and 2 (DM)"]),
    ("E", "Congenital endocrine disease", ["Thyroglossal duct cyst"]),
    ("F", "Endocrine vascular diseases", ["Postpartum pituitary necrosis (Sheehan necrosis)"]),
    ("G", "Endocrine neoplasms", ["Adrenal", "Pancreas (insulinoma)", "Parathyroid", "Pituitary (adenoma, non-functioning tumor, craniopharyngioma)", "Thyroid (adenoma and follicular, papillary and medullary carcinomas, euthyroid goiter)", "Other neoplasms (multiple endocrine neoplasia types 1 and 2, pheochromocytoma)"]),
    ("H", "Infectious endocrine diseases", ["Infectious thyroiditis", "Waterhouse-Friderichsen syndrome"]),
   ]},

  {"code": "IM", "name": "Immunological", "full": "Immunological System", "weight": 8, "week": 8, "reinforce": 10,
   "items": [
    (1, "Thymus embryology", "A", 0, "Describe embryological development of the thymus."),
    (2, "Lymphoid organ histology", "A", 0, "Describe microscopic anatomy of lymphoid organs."),
    (3, "Histocompatibility antigens and disease", "M", 0, "Describe structure and function of histocompatibility antigens and their associated diseases."),
    (4, "Lymphatic drainage", "A", 0, "Describe location and drainage patterns of lymphatic vessels."),
    (5, "Humoral and cell-mediated immunity", "M", 0, "Explain functions of cells, antibodies, and cytokines in humoral and cell-mediated immunity."),
    (6, "Cell and cytokine signaling in injury and infection", "M", 0, "Explain pathways of cellular and cytokine signaling in response to injury, infection, and foreign bodies."),
    (7, "Complement", "M", 0, "Explain structure, function, and pathways of complement compounds."),
    (8, "Lymphatic organ function", "P", 0, "Explain mechanisms, factors affecting, functions, and control of lymphatic organs."),
    (9, "Lymph composition and transport", "P", 0, "Explain composition, function, and transport of lymphatic fluid."),
    (10, "Immune biochemistry and nutrition", "B", 1, "Explain biochemistry of proteins, carbohydrates, lipids, vitamins, minerals, and co-factors, and biochemical processes and associated constituents involved in immunological function and pathology."),
    (11, "Lymph biochemistry", "B", 0, "Explain biochemistry of synthesis and degradation of lymphatic fluid and its components."),
    (12, "Immunogenetics", "B", 0, GENE.format("immunological")),
    (13, "Innate and adaptive immune activation", "M", 0, IMMUNE),
    (14, "Systemic pathogens", "M", 0, MICROBE),
   ],
   "condNum": 15,
   "categories": [
    ("A", "Congenital immunodeficiency diseases", ["Common variable immunodeficiency", "DiGeorge syndrome", "Selective IgA deficiency", "Severe combined immunodeficiency", "X-linked agammaglobulinemia"]),
    ("B", "Acquired immunodeficiency diseases", ["Drug-induced immunodeficiencies", "Human immunodeficiency virus (HIV)/acquired immune deficiency syndrome (AIDS)"]),
    ("C", "Diseases of hypersensitivity", ["Type I (anaphylaxis)", "Type II (autoimmune hemolytic anemia, Goodpasture syndrome, myasthenia gravis [MG])", "Type III (systemic lupus erythematosus [SLE], polyarteritis nodosa, poststreptococcal glomerulonephritis, rheumatoid arthritis)", "Type IV (granulomatous inflammation, transplant rejection)"]),
    ("D", "Other autoimmune diseases", ["Progressive systemic sclerosis (scleroderma)", "Rheumatic fever", "Sjögren syndrome"]),
    ("E", "Diseases of amyloids", ["Primary amyloidosis", "Secondary amyloidosis"]),
    ("F", "Systemic infectious diseases", ["Erythema infectiosum (fifth disease)", "Haemophilus influenzae type b", "Influenza", "Measles", "Mononucleosis", "Mumps", "Roseola infantum", "Rubella", "Scarlet fever", "Toxoplasmosis"]),
   ]},

  {"code": "PU", "name": "Pulmonary", "full": "Pulmonary System and Upper Respiratory Tract", "weight": 8, "week": 9, "reinforce": 11,
   "items": [
    (1, "Respiratory embryology", "A", 0, "Describe embryological development of respiratory tract."),
    (2, "Respiratory histology", "A", 0, "Describe microscopic anatomy of respiratory tract."),
    (3, "Upper respiratory tract", "A", 0, "Describe boundaries and anatomical structures associated with upper respiratory tract organs."),
    (4, "Thorax, pleura, lungs, and mediastinum", "A", 0, "Describe boundaries and components of thorax in relation to pleura, lungs, heart, and mediastinum."),
    (5, "Pulmonary blood flow and airflow", "AP", 0, "Describe circulation of blood and flow of air in lungs."),
    (6, "Ventilation", "P", 0, "Explain mechanisms, functions, regulation, and factors affecting ventilation."),
    (7, "Gas exchange and tissue perfusion", "P", 0, "Explain mechanisms, functions, regulation, and factors affecting gas exchange and tissue perfusion."),
    (8, "Blood gas transport", "P", 0, "Explain transport and regulation of blood gases."),
    (9, "Pulmonary biochemistry and nutrition", "B", 1, BIOCHEM.format("pulmonary")),
    (10, "Pulmonary genetics", "B", 0, GENE.format("pulmonary")),
    (11, "Energy production and the respiratory system", "B", 0, "Explain biochemistry of energy production and utilization as it relates to respiratory system."),
    (12, "Immune responses in pulmonary disease", "M", 0, IMMUNE),
    (13, "Pulmonary pathogens", "M", 0, MICROBE),
   ],
   "condNum": 14,
   "categories": [
    ("A", "Restrictive pulmonary diseases", ["Respiratory distress syndrome", "Idiopathic pulmonary fibrosis", "Pneumoconiosis", "Sarcoidosis"]),
    ("B", "Obstructive pulmonary diseases", ["Asthma", "Bronchiectasis", "Chronic bronchitis", "Emphysema"]),
    ("C", "Diseases of the upper respiratory tract", ["Bronchitis", "Epiglottitis", "Laryngitis", "Rhinitis", "Sinusitis", "Pharyngitis", "Tonsillitis"]),
    ("D", "Disorders of the pleural cavity and lung expansion", ["Chylothorax", "Hemothorax", "Obstructive atelectasis", "Pleural fibrosis (asbestosis)", "Pneumothorax"]),
    ("E", "Pulmonary vascular disease", ["Pulmonary edema", "Pulmonary emboli", "Pulmonary infarction"]),
    ("F", "Neoplasms of the pulmonary system and upper respiratory tract", ["Adenocarcinomas", "Bronchial carcinoid", "Esophageal", "Laryngeal", "Mesothelioma", "Nasopharyngeal carcinoma", "Polyps", "Small-cell carcinoma", "Non-small-cell carcinoma"]),
    ("G", "Congenital pulmonary diseases", ["Cystic fibrosis (CF)", "Tracheoesophageal fistula"]),
    ("H", "Infectious diseases of the pulmonary system and upper respiratory tract", ["Atypical pneumonia", "Bronchopneumonia", "Diphtheria", "Fungal pneumonia", "Lobar pneumonia", "Lung abscess", "Pertussis", "Respiratory syncytial virus (RSV)", "Tuberculosis (TB)", "Coronaviruses"]),
   ]},

  {"code": "HE", "name": "Hematopoietic", "full": "Hematopoietic System", "weight": 6, "week": 10, "reinforce": 12,
   "items": [
    (1, "Blood cell histology, origin, and maturation", "A", 0, "Describe microscopic anatomy, origins, and maturation of blood cells."),
    (2, "Blood cells and plasma", "P", 0, "Describe composition and explain function and regulation of blood cells and plasma."),
    (3, "Blood cell synthesis and breakdown", "PB", 0, "Describe synthesis and degradation of blood cells."),
    (4, "Hematopoiesis and hemostasis", "P", 0, "Explain mechanisms and factors affecting hematopoiesis and hemostasis."),
    (5, "Hemoglobin and hematologic biochemistry", "B", 1, "Explain biochemistry of proteins, carbohydrates, lipids, vitamins, minerals, and co-factors as they relate to hematopoietic function, hemostasis, and hemoglobin function, formation, and pathology."),
    (6, "Hematologic genetics", "B", 0, GENE.format("hematopoietic")),
    (7, "Immune responses in hematologic disease", "M", 0, IMMUNE),
    (8, "Blood-borne pathogens", "M", 0, MICROBE),
   ],
   "condNum": 9,
   "categories": [
    ("A", "Diseases of blood cell production", ["Anemias (macrocytic, microcytic, aplastic)", "Polycythemia (vera, secondary)"]),
    ("B", "Diseases of blood cell lysis", ["Hemolytic anemia (sickle cell, thalassemia, G6PD deficiency, spherocytosis)", "Hemolytic disease of the newborn (erythroblastosis fetalis)"]),
    ("C", "Clotting abnormalities", ["Disseminated intravascular coagulation (DIC)", "Hemophilia", "Immune thrombocytopenic purpura (ITP)", "Von Willebrand disease", "Vitamin K deficiency"]),
    ("D", "Blood and lymph neoplasms", ["Leukemias", "Lymphomas (Hodgkin, non-Hodgkin)", "Multiple myeloma"]),
    ("E", "Infectious diseases of the blood", ["Babesiosis", "Malaria", "Schistosomiasis"]),
   ]},

  {"code": "IN", "name": "Integumentary", "full": "Integumentary System", "weight": 6, "week": 11, "reinforce": 12,
   "items": [
    (1, "Skin layers and the dermal-epidermal junction", "A", 0, "Describe microscopic anatomy, derivations, and differentiating features of skin layers and dermal-epidermal junction."),
    (2, "Ectoderm embryology", "A", 0, "Describe embryological development of the ectoderm."),
    (3, "Membrane transport and membrane potential", "P", 0, "Explain function of membrane constituents and mechanisms governing transport across cell membranes, osmosis, membrane potential, and ionic equilibrium."),
    (4, "Thermoregulation", "P", 0, "Explain principles of thermal physiology, including regulation of body temperature."),
    (5, "Skin biochemistry and nutrition", "B", 1, "Explain biochemistry of proteins, carbohydrates, lipids, vitamins, minerals, and co-factors as they relate to the integumentary system."),
    (6, "Antioxidants and free radical scavengers", "B", 1, "Explain biochemistry of non-vitamin antioxidants and free radical scavengers as they relate to integumentary function and pathology."),
    (7, "Skin genetics", "B", 0, GENE.format("integumentary")),
    (8, "Cell adaptation, injury, pigmentation, and neoplasia", "X", 0, "Explain processes relating to adaptive changes, cellular injury, pigmentation, infiltration, and neoplasia."),
    (9, "Infection principles in skin disease", "M", 0, "Explain principles of infectious disease in dermatological pathologies, including normal flora, stages of infection, and characteristics of pathogenesis."),
    (10, "Skin trauma and wound healing", "X", 0, "Explain complications and clinical characteristics of skin trauma and healing mechanisms."),
    (11, "Immune responses in skin disease", "M", 0, IMMUNE),
    (12, "Skin pathogens", "M", 0, MICROBE),
   ],
   "condNum": 13,
   "categories": [
    ("A", "Pigmentation changes of the skin", ["Nevocellular nevus", "Vitiligo"]),
    ("B", "Acute inflammatory skin conditions", ["Atopic dermatitis (eczema)", "Contact dermatitis", "Erythema multiforme", "Urticaria"]),
    ("C", "Chronic inflammatory skin conditions", ["Acne rosacea", "Lichen planus", "Psoriasis"]),
    ("D", "Blistering diseases", ["Epidermolysis bullosa", "Pemphigoid", "Pemphigus"]),
    ("E", "Genetic skin conditions", ["Albinism", "Ehlers-Danlos syndrome"]),
    ("F", "Benign and premalignant skin lesions", ["Actinic keratosis", "Dysplastic nevi", "Seborrheic keratosis"]),
    ("G", "Malignant skin neoplasms", ["Basal cell carcinoma", "Squamous cell carcinoma", "Melanoma"]),
    ("H", "Infectious skin diseases", ["Acne vulgaris", "Candidiasis", "Cellulitis", "Erysipelas", "Erythema nodosum", "Folliculitis", "Impetigo", "Methicillin-resistant Staphylococcus aureus (MRSA)", "Molluscum contagiosum", "Tinea", "Verrucae", "Wound infection/needle stick"]),
   ]},
]


def category_seas(title):
    """Default SEA tags for a condition category (our classification)."""
    t = title.lower()
    if "infect" in t or "std" in t:
        return "MX", 0
    if any(k in t for k in ("immunodeficien", "hypersensitivity", "autoimmune", "amyloid")):
        return "MX", 0
    if any(k in t for k in ("nutritional", "deficiency", "malabsorption")):
        return "XB", 1
    if "congenital" in t or "genetic" in t:
        return "XB", 0
    return "X", 0
