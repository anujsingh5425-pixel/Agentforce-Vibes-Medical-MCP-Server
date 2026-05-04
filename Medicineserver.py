from mcp.server.fastmcp import FastMCP
from pydantic import Field

def load_hospital_data():
    with open("patient_qa.txt", "r", encoding="utf-8") as f:
        return f.read()

mcp = FastMCP("MedicineserverMCP")

Medicines = [
  {
    "name": "Paracetamol",
    "strength": "500mg",
    "indication": "Fever, Pain relief",
    "symptoms": "Fever, headache",
    "category": "Painkiller",
    "prescription_required": "no",
    "side_effects": "Nausea, rash",
    "contraindications": "Liver disease",
    "interactions": "Alcohol",
    "alcohol_advice": "Yes",
    "stock": 120,
    "price": 50,
    "expiry_date": "2027-05-12",
    "batch_number": "BATCH101",
    "max_daily_dose": 50,
    "typical_dosage": 45,
    "available": "yes"
  },
  {
    "name": "Ibuprofen",
    "strength": "400mg",
    "indication": "Pain, inflammation",
    "symptoms": "Joint pain, swelling",
    "category": "Painkiller",
    "prescription_required": "no",
    "side_effects": "Stomach pain",
    "contraindications": "Ulcer",
    "interactions": "Aspirin",
    "alcohol_advice": "No",
    "stock": 80,
    "price": 40,
    "expiry_date": "2026-11-20",
    "batch_number": "BATCH102",
    "max_daily_dose": 80,
    "typical_dosage": 70,
    "available": "yes"
  },
  {
    "name": "Amoxicillin",
    "strength": "250mg",
    "indication": "Bacterial infection",
    "symptoms": "Throat infection",
    "category": "Antibiotic",
    "prescription_required": "yes",
    "side_effects": "Diarrhea",
    "contraindications": "Penicillin allergy",
    "interactions": "Methotrexate",
    "alcohol_advice": "Consult Doctor",
    "stock": 60,
    "price": 30,
    "expiry_date": "2025-12-15",
    "batch_number": "BATCH103",
    "max_daily_dose": 120,
    "typical_dosage": 100,
    "available": "yes"
  },
  {
    "name": "Azithromycin",
    "strength": "500mg",
    "indication": "Infection",
    "symptoms": "Chest infection",
    "category": "Antibiotic",
    "prescription_required": "yes",
    "side_effects": "Nausea",
    "contraindications": "Liver issues",
    "interactions": "Antacids",
    "alcohol_advice": "Consult Doctor",
    "stock": 0,
    "price": 20,
    "expiry_date": "2025-08-10",
    "batch_number": "BATCH104",
    "max_daily_dose": 150,
    "typical_dosage": 130,
    "available": "no"
  },
  {
    "name": "Cetirizine",
    "strength": "10mg",
    "indication": "Allergy relief",
    "symptoms": "Sneezing, cold",
    "category": "Antihistamine",
    "prescription_required": "no",
    "side_effects": "Drowsiness",
    "contraindications": "Kidney disease",
    "interactions": "Alcohol",
    "alcohol_advice": "Yes",
    "stock": 200,
    "price": 60,
    "expiry_date": "2027-01-01",
    "batch_number": "BATCH105",
    "max_daily_dose": 30,
    "typical_dosage": 25,
    "available": "yes"
  },
  {
    "name": "Metformin",
    "strength": "500mg",
    "indication": "Diabetes control",
    "symptoms": "High sugar",
    "category": "Antidiabetic",
    "prescription_required": "yes",
    "side_effects": "Diarrhea",
    "contraindications": "Kidney disease",
    "interactions": "Insulin",
    "alcohol_advice": "Consult Doctor",
    "stock": 150,
    "price": 70,
    "expiry_date": "2026-09-14",
    "batch_number": "BATCH106",
    "max_daily_dose": 90,
    "typical_dosage": 80,
    "available": "yes"
  },
  {
    "name": "Aspirin",
    "strength": "75mg",
    "indication": "Blood thinning",
    "symptoms": "Heart risk",
    "category": "Antiplatelet",
    "prescription_required": "yes",
    "side_effects": "Bleeding",
    "contraindications": "Ulcer",
    "interactions": "Ibuprofen",
    "alcohol_advice": "No",
    "stock": 90,
    "price": 40,
    "expiry_date": "2027-03-22",
    "batch_number": "BATCH107",
    "max_daily_dose": 40,
    "typical_dosage": 35,
    "available": "yes"
  },
  {
    "name": "Omeprazole",
    "strength": "20mg",
    "indication": "Acidity",
    "symptoms": "GERD",
    "category": "Antacid",
    "prescription_required": "no",
    "side_effects": "Headache",
    "contraindications": "Liver disease",
    "interactions": "Clopidogrel",
    "alcohol_advice": "Yes",
    "stock": 110,
    "price": 50,
    "expiry_date": "2026-06-30",
    "batch_number": "BATCH108",
    "max_daily_dose": 100,
    "typical_dosage": 85,
    "available": "yes"
  },
  {
    "name": "Pantoprazole",
    "strength": "40mg",
    "indication": "Acid reflux",
    "symptoms": "Acidity",
    "category": "Antacid",
    "prescription_required": "no",
    "side_effects": "Diarrhea",
    "contraindications": "Osteoporosis",
    "interactions": "Ketoconazole",
    "alcohol_advice": "Yes",
    "stock": 0,
    "price": 30,
    "expiry_date": "2025-10-05",
    "batch_number": "BATCH109",
    "max_daily_dose": 120,
    "typical_dosage": 100,
    "available": "no"
  },
  {
    "name": "Dolo 650",
    "strength": "650mg",
    "indication": "Fever",
    "symptoms": "High fever",
    "category": "Painkiller",
    "prescription_required": "no",
    "side_effects": "Nausea",
    "contraindications": "Liver disease",
    "interactions": "Alcohol",
    "alcohol_advice": "Yes",
    "stock": 300,
    "price": 100,
    "expiry_date": "2027-12-01",
    "batch_number": "BATCH110",
    "max_daily_dose": 60,
    "typical_dosage": 55,
    "available": "yes"
  },
  {
    "name": "Crocin",
    "strength": "500mg",
    "indication": "Fever",
    "symptoms": "Mild fever",
    "category": "Painkiller",
    "prescription_required": "no",
    "side_effects": "Rash",
    "contraindications": "Liver issue",
    "interactions": "Alcohol",
    "alcohol_advice": "Yes",
    "stock": 180,
    "price": 80,
    "expiry_date": "2026-04-18",
    "batch_number": "BATCH111",
    "max_daily_dose": 45,
    "typical_dosage": 40,
    "available": "yes"
  },
  {
    "name": "ORS Powder",
    "strength": "Sachet",
    "indication": "Dehydration",
    "symptoms": "Diarrhea",
    "category": "Rehydration",
    "prescription_required": "no",
    "side_effects": "None",
    "contraindications": "None",
    "interactions": "None",
    "alcohol_advice": "Yes",
    "stock": 75,
    "price": 30,
    "expiry_date": "2028-02-01",
    "batch_number": "BATCH112",
    "max_daily_dose": 20,
    "typical_dosage": 18,
    "available": "yes"
  },
  {
    "name": "Insulin",
    "strength": "Injection",
    "indication": "Diabetes",
    "symptoms": "High sugar",
    "category": "Hormone",
    "prescription_required": "yes",
    "side_effects": "Hypoglycemia",
    "contraindications": "Kidney issue",
    "interactions": "Metformin",
    "alcohol_advice": "Consult Doctor",
    "stock": 40,
    "price": 20,
    "expiry_date": "2025-11-11",
    "batch_number": "BATCH113",
    "max_daily_dose": 500,
    "typical_dosage": 450,
    "available": "yes"
  },
  {
    "name": "Atorvastatin",
    "strength": "10mg",
    "indication": "Cholesterol",
    "symptoms": "High LDL",
    "category": "Statin",
    "prescription_required": "yes",
    "side_effects": "Muscle pain",
    "contraindications": "Liver disease",
    "interactions": "Alcohol",
    "alcohol_advice": "No",
    "stock": 95,
    "price": 50,
    "expiry_date": "2027-07-07",
    "batch_number": "BATCH114",
    "max_daily_dose": 150,
    "typical_dosage": 130,
    "available": "yes"
  },
  {
    "name": "Losartan",
    "strength": "50mg",
    "indication": "BP control",
    "symptoms": "Hypertension",
    "category": "Antihypertensive",
    "prescription_required": "yes",
    "side_effects": "Dizziness",
    "contraindications": "Kidney disease",
    "interactions": "Diuretics",
    "alcohol_advice": "Consult Doctor",
    "stock": 70,
    "price": 40,
    "expiry_date": "2026-08-19",
    "batch_number": "BATCH115",
    "max_daily_dose": 140,
    "typical_dosage": 120,
    "available": "yes"
  },
  {
    "name": "Hydroxychloroquine",
    "strength": "200mg",
    "indication": "Autoimmune",
    "symptoms": "Arthritis",
    "category": "Antimalarial",
    "prescription_required": "yes",
    "side_effects": "Vision issues",
    "contraindications": "Eye disease",
    "interactions": "Digoxin",
    "alcohol_advice": "No",
    "stock": 0,
    "price": 25,
    "expiry_date": "2025-09-09",
    "batch_number": "BATCH116",
    "max_daily_dose": 200,
    "typical_dosage": 180,
    "available": "no"
  },
  {
    "name": "Salbutamol",
    "strength": "Inhaler",
    "indication": "Asthma",
    "symptoms": "Breathlessness",
    "category": "Bronchodilator",
    "prescription_required": "no",
    "side_effects": "Tremor",
    "contraindications": "Heart disease",
    "interactions": "Beta blockers",
    "alcohol_advice": "Yes",
    "stock": 55,
    "price": 20,
    "expiry_date": "2026-12-25",
    "batch_number": "BATCH117",
    "max_daily_dose": 180,
    "typical_dosage": 160,
    "available": "yes"
  },
  {
    "name": "Levocetirizine",
    "strength": "5mg",
    "indication": "Allergy",
    "symptoms": "Cold",
    "category": "Antihistamine",
    "prescription_required": "no",
    "side_effects": "Sleepiness",
    "contraindications": "Kidney issue",
    "interactions": "Alcohol",
    "alcohol_advice": "Yes",
    "stock": 130,
    "price": 50,
    "expiry_date": "2027-01-20",
    "batch_number": "BATCH118",
    "max_daily_dose": 35,
    "typical_dosage": 30,
    "available": "yes"
  },
  {
    "name": "Ranitidine",
    "strength": "150mg",
    "indication": "Acidity",
    "symptoms": "Ulcer",
    "category": "Antacid",
    "prescription_required": "no",
    "side_effects": "Headache",
    "contraindications": "Kidney issue",
    "interactions": "Warfarin",
    "alcohol_advice": "Yes",
    "stock": 0,
    "price": 20,
    "expiry_date": "2025-06-15",
    "batch_number": "BATCH119",
    "max_daily_dose": 60,
    "typical_dosage": 50,
    "available": "no"
  },
  {
    "name": "Clopidogrel",
    "strength": "75mg",
    "indication": "Blood thinner",
    "symptoms": "Stroke prevention",
    "category": "Antiplatelet",
    "prescription_required": "yes",
    "side_effects": "Bleeding",
    "contraindications": "Ulcer",
    "interactions": "Omeprazole",
    "alcohol_advice": "No",
    "stock": 85,
    "price": 40,
    "expiry_date": "2026-03-03",
    "batch_number": "BATCH120",
    "max_daily_dose": 220,
    "typical_dosage": 200,
    "available": "yes"
  },
  {
    "name": "Diclofenac",
    "strength": "50mg",
    "indication": "Pain relief",
    "symptoms": "Muscle pain",
    "category": "NSAID",
    "prescription_required": "yes",
    "side_effects": "Stomach pain",
    "contraindications": "Ulcer",
    "interactions": "Aspirin",
    "alcohol_advice": "No",
    "stock": 60,
    "price": 30,
    "expiry_date": "2026-07-17",
    "batch_number": "BATCH121",
    "max_daily_dose": 90,
    "typical_dosage": 80,
    "available": "yes"
  },
  {
    "name": "Amikacin",
    "strength": "Injection",
    "indication": "Severe infection",
    "symptoms": "Bacterial infection",
    "category": "Antibiotic",
    "prescription_required": "yes",
    "side_effects": "Kidney damage",
    "contraindications": "Renal issue",
    "interactions": "Furosemide",
    "alcohol_advice": "No",
    "stock": 25,
    "price": 10,
    "expiry_date": "2025-12-30",
    "batch_number": "BATCH122",
    "max_daily_dose": 300,
    "typical_dosage": 270,
    "available": "yes"
  },
  {
    "name": "Ciprofloxacin",
    "strength": "500mg",
    "indication": "Infection",
    "symptoms": "UTI",
    "category": "Antibiotic",
    "prescription_required": "yes",
    "side_effects": "Nausea",
    "contraindications": "Tendon issue",
    "interactions": "Antacids",
    "alcohol_advice": "No",
    "stock": 100,
    "price": 50,
    "expiry_date": "2026-10-10",
    "batch_number": "BATCH123",
    "max_daily_dose": 110,
    "typical_dosage": 95,
    "available": "yes"
  },
  {
    "name": "Dexamethasone",
    "strength": "4mg",
    "indication": "Inflammation",
    "symptoms": "Allergy",
    "category": "Steroid",
    "prescription_required": "yes",
    "side_effects": "Weight gain",
    "contraindications": "Infection",
    "interactions": "NSAIDs",
    "alcohol_advice": "No",
    "stock": 45,
    "price": 20,
    "expiry_date": "2026-01-05",
    "batch_number": "BATCH124",
    "max_daily_dose": 70,
    "typical_dosage": 60,
    "available": "yes"
  },
  {
    "name": "Montelukast",
    "strength": "10mg",
    "indication": "Asthma",
    "symptoms": "Allergy",
    "category": "Leukotriene blocker",
    "prescription_required": "no",
    "side_effects": "Headache",
    "contraindications": "Liver issue",
    "interactions": "Phenobarbital",
    "alcohol_advice": "Yes",
    "stock": 75,
    "price": 30,
    "expiry_date": "2027-02-11",
    "batch_number": "BATCH125",
    "max_daily_dose": 130,
    "typical_dosage": 110,
    "available": "yes"
  }
]

@mcp.tool(name= "list_medicines", description="Get list of all medicines")
def list_medicines():
    return [medicine["name"] for medicine in Medicines]

@mcp.tool(name="search_medicines", description="Search medicines by name or indication and return complete details")
def search_medicines(query: str):
    results = []
    for medicine in Medicines:
        if query.lower() in medicine["name"].lower() or query.lower() in medicine["indication"].lower():
            results.append(medicine)
    return results


@mcp.resource(
    name="hospital_qa_data",
    uri="hospital://qa-data",
    description="Hospital Q&A knowledge base"
)
def hospital_qa_resource():
    return load_hospital_data()

@mcp.tool(name="search_hospital_qa", description="Search hospital Q&A from knowledge base")
def search_hospital_qa(query: str):

    data = hospital_qa_resource()

    blocks = data.split("\n\n")
    results = []

    query_words = query.lower().split()

    for block in blocks:
        score = sum(1 for word in query_words if word in block.lower())

        if score > 0:
            results.append({
                "score": score,
                "answer": block.strip()
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:3]


    


# ---------------------------
if __name__ == "__main__":
    mcp.run(transport="stdio")
