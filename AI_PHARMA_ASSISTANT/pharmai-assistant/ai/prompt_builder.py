"""
Dynamic prompt builder for personalized AI responses.
Constructs prompts that consider user's medical profile.
"""

def build_medication_prompt(medication_name, user_profile):
    """
    Build a personalized medication information prompt.
    
    Args:
        medication_name: Name of the medication to query
        user_profile: User's medical profile dictionary
    
    Returns:
        Personalized prompt string
    """
    age = user_profile.get('age', 'Not specified')
    allergies = user_profile.get('known_allergies', [])
    conditions = user_profile.get('existing_conditions', [])
    medications = user_profile.get('current_medications', [])
    
    prompt = f"""You are PharmAI, a medical information assistant. Provide detailed information about {medication_name}.

IMPORTANT: You are assisting a {age}-year-old patient with the following medical profile:
- Known Allergies: {', '.join(allergies) if allergies else 'None reported'}
- Existing Conditions: {', '.join(conditions) if conditions else 'None reported'}
- Current Medications: {', '.join(medications) if medications else 'None reported'}

Please provide information about {medication_name} including:

1. **Basic Information**: What it is and what it's used for
2. **Dosage**: Typical dosage information (note: always consult doctor for specific dosing)
3. **Side Effects**: Common and serious side effects
4. **Safety Precautions**: Important safety information

CRITICAL - Check for interactions and contraindications with:
- Patient's known allergies
- Patient's existing conditions
- Patient's current medications

If you identify ANY potential interactions, allergies, or contraindications, clearly mark them with:
- ⚠️ WARNING for interactions or concerns
- 🚨 DANGER for serious contraindications or allergy risks

Personalize the response based on the patient's age and medical profile.

End with this disclaimer:
---
**Disclaimer:** This information is AI-generated and does not replace professional medical advice. Always consult a licensed healthcare provider before taking any medication.
---"""
    
    return prompt

def build_general_medication_prompt(query, user_profile):
    """
    Build a personalized prompt for general medication questions.
    
    Args:
        query: User's question about medications
        user_profile: User's medical profile dictionary
    
    Returns:
        Personalized prompt string
    """
    age = user_profile.get('age', 'Not specified')
    allergies = user_profile.get('known_allergies', [])
    conditions = user_profile.get('existing_conditions', [])
    medications = user_profile.get('current_medications', [])
    
    prompt = f"""You are PharmAI, a medical information assistant specialized in providing medication guidance.

Patient Profile:
- Age: {age} years old
- Known Allergies: {', '.join(allergies) if allergies else 'None reported'}
- Existing Medical Conditions: {', '.join(conditions) if conditions else 'None reported'}
- Currently Taking: {', '.join(medications) if medications else 'No medications reported'}

Patient Question: {query}

Please respond by:
1. Addressing the specific question about medications
2. Considering the patient's medical profile, allergies, and current medications
3. Checking for potential drug interactions with current medications
4. Checking for allergy-related contraindications
5. Personalizing advice based on patient's age and conditions

IMPORTANT WARNINGS:
- If there are medication interactions with any current medications, clearly indicate with ⚠️ WARNING
- If there are serious contraindications or allergy risks, clearly indicate with 🚨 DANGER
- Always emphasize the importance of consulting with a licensed healthcare provider

End with this disclaimer:
---
**Disclaimer:** This information is AI-generated and does not replace professional medical advice. Always consult a licensed healthcare provider before taking any medication.
---"""
    
    return prompt

def build_system_prompt(user_profile):
    """
    Build a system prompt that includes user's medical context.
    
    Args:
        user_profile: User's medical profile dictionary
    
    Returns:
        System prompt string
    """
    age = user_profile.get('age', 'Not specified')
    allergies = user_profile.get('known_allergies', [])
    conditions = user_profile.get('existing_conditions', [])
    medications = user_profile.get('current_medications', [])
    
    system_prompt = f"""You are PharmAI Assistant, an AI-powered medical information specialist.

You are helping a {age}-year-old patient with:
- Allergies: {', '.join(allergies) if allergies else 'None'}
- Conditions: {', '.join(conditions) if conditions else 'None'}
- Current Medications: {', '.join(medications) if medications else 'None'}

Your responsibilities:
1. Provide accurate medication and drug information
2. Explain side effects, dosage, and usage
3. CHECK FOR INTERACTIONS with the patient's current medications
4. CHECK FOR ALLERGY CONTRAINDICATIONS
5. Personalize responses based on patient's age and health profile
6. Always include appropriate warnings for interactions or contraindications
7. Always end responses with medical disclaimers

Be professional, clear, and focused on patient safety."""
    
    return system_prompt
