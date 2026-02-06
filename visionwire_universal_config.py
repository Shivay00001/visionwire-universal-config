"""
VisionWire AI - Universal Configuration
ALL Classes, ALL Subjects, ALL Exams, ALL Languages
Complete Indian Education System Coverage
"""

import json
from typing import Dict, List

class UniversalConfig:
    """Complete configuration for Indian education system"""
    
    # ============= ALL CLASSES =============
    CLASSES = {
        'primary': ['1', '2', '3', '4', '5'],
        'middle': ['6', '7', '8'],
        'secondary': ['9', '10'],
        'senior_secondary': ['11', '12'],
        'undergraduate': ['UG Year 1', 'UG Year 2', 'UG Year 3', 'UG Year 4'],
        'postgraduate': ['PG Year 1', 'PG Year 2']
    }
    
    # ============= ALL SUBJECTS BY CLASS =============
    SUBJECTS = {
        # Class 1-5 (Primary)
        '1-5': {
            'core': ['Hindi', 'English', 'Mathematics', 'Environmental Studies', 'General Knowledge'],
            'optional': ['Art & Craft', 'Music', 'Physical Education', 'Computer']
        },
        
        # Class 6-8 (Middle School)
        '6-8': {
            'core': ['Hindi', 'English', 'Mathematics', 'Science', 'Social Science'],
            'optional': ['Sanskrit', 'Computer Science', 'Art', 'Physical Education', 'Third Language']
        },
        
        # Class 9-10 (Secondary)
        '9-10': {
            'core': ['Hindi', 'English', 'Mathematics', 'Science', 'Social Science'],
            'optional': ['Sanskrit', 'Computer Applications', 'Physical Education', 'Art', 'Home Science', 'Third Language']
        },
        
        # Class 11-12 Science Stream
        '11-12-science': {
            'core': ['Physics', 'Chemistry', 'Biology', 'Mathematics', 'English', 'Physical Education'],
            'optional': ['Computer Science', 'Psychology', 'Home Science', 'Hindi']
        },
        
        # Class 11-12 Commerce Stream
        '11-12-commerce': {
            'core': ['Accountancy', 'Business Studies', 'Economics', 'English', 'Mathematics/Applied Mathematics'],
            'optional': ['Computer Science', 'Physical Education', 'Hindi', 'Entrepreneurship', 'Informatics Practices']
        },
        
        # Class 11-12 Arts/Humanities Stream
        '11-12-arts': {
            'core': ['History', 'Political Science', 'Geography', 'Economics', 'English', 'Hindi'],
            'optional': ['Psychology', 'Sociology', 'Philosophy', 'Physical Education', 'Home Science', 'Fine Arts', 'Music']
        },
        
        # Undergraduate (Engineering)
        'ug-engineering': {
            'core': ['Engineering Mathematics', 'Physics', 'Chemistry', 'Engineering Drawing', 'Programming'],
            'specialization': ['Computer Science', 'Mechanical', 'Civil', 'Electrical', 'Electronics', 'Chemical']
        },
        
        # Undergraduate (Medical)
        'ug-medical': {
            'core': ['Anatomy', 'Physiology', 'Biochemistry', 'Pathology', 'Pharmacology', 'Microbiology', 
                    'Forensic Medicine', 'Community Medicine', 'Medicine', 'Surgery', 'Pediatrics', 'Obstetrics & Gynecology']
        },
        
        # Undergraduate (Arts/Science/Commerce)
        'ug-general': {
            'science': ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'Computer Science', 'Statistics', 'Geology'],
            'arts': ['History', 'Political Science', 'Economics', 'Sociology', 'Psychology', 'English Literature', 'Hindi Literature', 'Philosophy'],
            'commerce': ['Accounting', 'Finance', 'Marketing', 'Business Management', 'Economics', 'Taxation']
        }
    }
    
    # ============= ALL EXAMS =============
    EXAMS = {
        # School Board Exams
        'school_boards': {
            'CBSE': ['Class 1-12', 'All subjects'],
            'ICSE': ['Class 1-10', 'All subjects'],
            'ISC': ['Class 11-12', 'All subjects'],
            'State Boards': [
                'UP Board', 'Maharashtra Board', 'Bihar Board', 'MP Board', 'Rajasthan Board',
                'Gujarat Board', 'Karnataka Board', 'Tamil Nadu Board', 'Kerala Board', 
                'West Bengal Board', 'AP Board', 'Telangana Board', 'Odisha Board',
                'Assam Board', 'Punjab Board', 'Haryana Board', 'Jharkhand Board',
                'Chhattisgarh Board', 'Uttarakhand Board', 'HP Board', 'J&K Board'
            ]
        },
        
        # Medical Entrance
        'medical': {
            'NEET UG': ['Physics', 'Chemistry', 'Biology'],
            'NEET PG': ['Medical subjects'],
            'AIIMS': ['Physics', 'Chemistry', 'Biology', 'General Knowledge'],
            'JIPMER': ['Physics', 'Chemistry', 'Biology'],
            'State Medical': ['All state PMTs']
        },
        
        # Engineering Entrance
        'engineering': {
            'JEE Main': ['Physics', 'Chemistry', 'Mathematics'],
            'JEE Advanced': ['Physics', 'Chemistry', 'Mathematics'],
            'BITSAT': ['Physics', 'Chemistry', 'Mathematics', 'English', 'Logical Reasoning'],
            'VITEEE': ['Physics', 'Chemistry', 'Mathematics'],
            'SRMJEEE': ['Physics', 'Chemistry', 'Mathematics'],
            'State Engineering': ['MHT CET', 'KCET', 'WBJEE', 'TS EAMCET', 'AP EAMCET', 'COMEDK', 'KEAM']
        },
        
        # Other Undergraduate
        'other_ug': {
            'CUET UG': ['Domain subjects', 'General Test'],
            'CLAT': ['Legal Reasoning', 'Logical Reasoning', 'English', 'GK', 'Quantitative'],
            'NDA': ['Mathematics', 'General Ability Test'],
            'AFCAT': ['General Awareness', 'Verbal', 'Numerical', 'Reasoning'],
            'BHU UET': ['Subject-specific'],
            'IPU CET': ['Subject-specific'],
            'DUET': ['Subject-specific']
        },
        
        # Postgraduate
        'postgraduate': {
            'GATE': ['All 27 papers - CS, EC, ME, CE, EE, etc.'],
            'CAT': ['Verbal', 'Data Interpretation', 'Quantitative'],
            'XAT': ['Verbal', 'Decision Making', 'Quantitative', 'GK'],
            'MAT': ['Language', 'Data Analysis', 'Mathematical', 'Intelligence'],
            'CMAT': ['Quantitative', 'Logical', 'Language', 'GK'],
            'NMAT': ['Language', 'Quantitative', 'Logical'],
            'SNAP': ['General English', 'Quantitative', 'Analytical', 'GK'],
            'CUET PG': ['Subject-specific'],
            'JAM': ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'Economics', 'Geology'],
            'CSIR NET': ['Life Sciences', 'Physical Sciences', 'Chemical Sciences', 'Earth Sciences', 'Mathematical Sciences']
        },
        
        # Government Jobs
        'government': {
            'UPSC': ['Civil Services', 'IFS', 'IES', 'CAPF', 'CDS'],
            'SSC': ['CGL', 'CHSL', 'JE', 'MTS', 'GD', 'Stenographer'],
            'Banking': ['IBPS PO', 'IBPS Clerk', 'IBPS RRB', 'SBI PO', 'SBI Clerk', 'RBI Grade B', 'NABARD'],
            'Railway': ['RRB NTPC', 'RRB JE', 'RRB ALP', 'RRB Group D'],
            'State PSC': ['All state civil services', 'State PCS'],
            'Teaching': ['CTET', 'State TETs', 'UGC NET', 'DSSSB', 'KVS', 'NVS'],
            'Defense': ['Army', 'Navy', 'Air Force', 'Paramilitary']
        },
        
        # Professional
        'professional': {
            'CA': ['Foundation', 'Intermediate', 'Final'],
            'CS': ['Foundation', 'Executive', 'Professional'],
            'CMA': ['Foundation', 'Intermediate', 'Final'],
            'ACCA': ['All levels'],
            'CFA': ['Level 1', 'Level 2', 'Level 3']
        },
        
        # International
        'international': {
            'SAT': ['Evidence-Based Reading', 'Mathematics'],
            'ACT': ['English', 'Math', 'Reading', 'Science'],
            'GRE': ['Verbal', 'Quantitative', 'Analytical Writing'],
            'GMAT': ['Verbal', 'Quantitative', 'Integrated Reasoning', 'AWA'],
            'TOEFL': ['Reading', 'Listening', 'Speaking', 'Writing'],
            'IELTS': ['Listening', 'Reading', 'Writing', 'Speaking'],
            'PTE': ['Speaking', 'Writing', 'Reading', 'Listening']
        }
    }
    
    # ============= ALL LANGUAGES =============
    LANGUAGES = {
        'primary': {
            'hindi': {'name': 'हिंदी', 'code': 'hi', 'script': 'Devanagari'},
            'english': {'name': 'English', 'code': 'en', 'script': 'Latin'}
        },
        
        'indian_languages': {
            'hindi': {'name': 'हिंदी', 'code': 'hi', 'speakers': '52.8 crore'},
            'bengali': {'name': 'বাংলা', 'code': 'bn', 'speakers': '9.7 crore'},
            'marathi': {'name': 'मराठी', 'code': 'mr', 'speakers': '8.3 crore'},
            'telugu': {'name': 'తెలుగు', 'code': 'te', 'speakers': '8.1 crore'},
            'tamil': {'name': 'தமிழ்', 'code': 'ta', 'speakers': '6.9 crore'},
            'gujarati': {'name': 'ગુજરાતી', 'code': 'gu', 'speakers': '5.5 crore'},
            'urdu': {'name': 'اردو', 'code': 'ur', 'speakers': '5.1 crore'},
            'kannada': {'name': 'ಕನ್ನಡ', 'code': 'kn', 'speakers': '4.4 crore'},
            'odia': {'name': 'ଓଡ଼ିଆ', 'code': 'or', 'speakers': '3.8 crore'},
            'malayalam': {'name': 'മലയാളം', 'code': 'ml', 'speakers': '3.5 crore'},
            'punjabi': {'name': 'ਪੰਜਾਬੀ', 'code': 'pa', 'speakers': '3.3 crore'},
            'assamese': {'name': 'অসমীয়া', 'code': 'as', 'speakers': '1.5 crore'},
            'maithili': {'name': 'मैथिली', 'code': 'mai', 'speakers': '1.4 crore'},
            'santali': {'name': 'ᱥᱟᱱᱛᱟᱲᱤ', 'code': 'sat', 'speakers': '73 lakh'},
            'kashmiri': {'name': 'कॉशुर', 'code': 'ks', 'speakers': '69 lakh'},
            'nepali': {'name': 'नेपाली', 'code': 'ne', 'speakers': '29 lakh'},
            'konkani': {'name': 'कोंकणी', 'code': 'kok', 'speakers': '25 lakh'},
            'sindhi': {'name': 'سنڌي', 'code': 'sd', 'speakers': '28 lakh'},
            'dogri': {'name': 'डोगरी', 'code': 'doi', 'speakers': '25 lakh'},
            'manipuri': {'name': 'মৈতৈলোন্', 'code': 'mni', 'speakers': '18 lakh'},
            'bodo': {'name': 'बड़ो', 'code': 'brx', 'speakers': '14 lakh'},
            'sanskrit': {'name': 'संस्कृतम्', 'code': 'sa', 'speakers': 'Classical'}
        },
        
        'international': {
            'english': {'name': 'English', 'code': 'en'},
            'spanish': {'name': 'Español', 'code': 'es'},
            'french': {'name': 'Français', 'code': 'fr'},
            'german': {'name': 'Deutsch', 'code': 'de'},
            'chinese': {'name': '中文', 'code': 'zh'},
            'japanese': {'name': '日本語', 'code': 'ja'},
            'korean': {'name': '한국어', 'code': 'ko'},
            'arabic': {'name': 'العربية', 'code': 'ar'},
            'russian': {'name': 'Русский', 'code': 'ru'},
            'portuguese': {'name': 'Português', 'code': 'pt'}
        }
    }
    
    # ============= SYLLABUS COVERAGE =============
    SYLLABUS_SOURCES = {
        'cbse': {
            'url': 'https://cbseacademic.nic.in',
            'classes': ['1-12'],
            'subjects': 'All core + optional'
        },
        'icse': {
            'url': 'https://cisce.org',
            'classes': ['1-10'],
            'subjects': 'All ICSE subjects'
        },
        'ncert': {
            'url': 'https://ncert.nic.in',
            'books': 'Class 1-12 all subjects',
            'format': 'PDF chapters'
        },
        'neet': {
            'syllabus': 'NCERT Class 11-12 PCB',
            'pattern': '180 MCQs (Physics 45, Chemistry 45, Biology 90)',
            'duration': '3 hours'
        },
        'jee': {
            'main': 'NCERT Class 11-12 PCM + Boards',
            'advanced': 'Deeper concepts, IIT level',
            'pattern': 'Main: 90 questions, Advanced: 48-54 questions'
        }
    }
    
    # ============= AGE GROUPS =============
    AGE_GROUPS = {
        'class_1-5': {'age': '6-10', 'level': 'Simple language, pictures, examples'},
        'class_6-8': {'age': '11-13', 'level': 'Moderate, concept building'},
        'class_9-10': {'age': '14-15', 'level': 'Board exam focus, detailed'},
        'class_11-12': {'age': '16-18', 'level': 'Advanced, entrance exam ready'},
        'undergraduate': {'age': '18-22', 'level': 'Professional, research-oriented'},
        'postgraduate': {'age': '22+', 'level': 'Expert, specialized'},
        'working_professional': {'age': '25+', 'level': 'Practical, job-focused'}
    }
    
    # ============= QUESTION TYPES =============
    QUESTION_TYPES = {
        'mcq': {
            'single_correct': 'One correct answer',
            'multiple_correct': 'Multiple answers possible',
            'assertion_reason': 'Statement 1 & 2 based',
            'passage_based': 'Comprehension + questions',
            'integer_type': 'Numeric answer'
        },
        'subjective': {
            'very_short': '1 mark, 1-2 lines',
            'short': '2-3 marks, 30-50 words',
            'long': '5-6 marks, 100-150 words',
            'very_long': '10+ marks, 250+ words'
        },
        'numerical': {
            'single_step': 'Direct formula application',
            'multi_step': 'Multiple calculations',
            'derivation': 'Prove the formula',
            'application': 'Real-world problem'
        },
        'practical': {
            'diagram': 'Draw and label',
            'experiment': 'Procedure, observation, result',
            'project': 'Research-based'
        }
    }
    
    # ============= DIFFICULTY LEVELS =============
    DIFFICULTY_PRESETS = {
        'easy_focused': {'easy': 60, 'medium': 30, 'hard': 10},
        'balanced': {'easy': 40, 'medium': 40, 'hard': 20},
        'moderate': {'easy': 30, 'medium': 50, 'hard': 20},
        'hard_focused': {'easy': 20, 'medium': 40, 'hard': 40},
        'competitive': {'easy': 10, 'medium': 40, 'hard': 50}
    }
    
    @staticmethod
    def get_subjects_for_class(class_num: str) -> List[str]:
        """Get all subjects for a class"""
        class_int = int(class_num) if class_num.isdigit() else 0
        
        if class_int <= 5:
            return UniversalConfig.SUBJECTS['1-5']['core'] + UniversalConfig.SUBJECTS['1-5']['optional']
        elif class_int <= 8:
            return UniversalConfig.SUBJECTS['6-8']['core'] + UniversalConfig.SUBJECTS['6-8']['optional']
        elif class_int <= 10:
            return UniversalConfig.SUBJECTS['9-10']['core'] + UniversalConfig.SUBJECTS['9-10']['optional']
        elif class_int <= 12:
            # Return all streams
            return (UniversalConfig.SUBJECTS['11-12-science']['core'] + 
                   UniversalConfig.SUBJECTS['11-12-commerce']['core'] + 
                   UniversalConfig.SUBJECTS['11-12-arts']['core'])
        else:
            return []
    
    @staticmethod
    def get_all_exams() -> List[str]:
        """Get list of all supported exams"""
        all_exams = []
        for category in UniversalConfig.EXAMS.values():
            all_exams.extend(category.keys())
        return all_exams
    
    @staticmethod
    def get_all_languages() -> List[str]:
        """Get list of all supported languages"""
        langs = list(UniversalConfig.LANGUAGES['indian_languages'].keys())
        langs.extend(UniversalConfig.LANGUAGES['international'].keys())
        return list(set(langs))
    
    @staticmethod
    def export_config() -> Dict:
        """Export complete configuration as JSON"""
        return {
            'classes': UniversalConfig.CLASSES,
            'subjects': UniversalConfig.SUBJECTS,
            'exams': UniversalConfig.EXAMS,
            'languages': UniversalConfig.LANGUAGES,
            'syllabus_sources': UniversalConfig.SYLLABUS_SOURCES,
            'age_groups': UniversalConfig.AGE_GROUPS,
            'question_types': UniversalConfig.QUESTION_TYPES,
            'difficulty_presets': UniversalConfig.DIFFICULTY_PRESETS
        }

# ============= USAGE EXAMPLE =============

if __name__ == "__main__":
    # Print summary
    print("="*70)
    print("VisionWire AI - Universal Configuration")
    print("="*70)
    
    print(f"\n📚 Total Classes: {sum(len(v) for v in UniversalConfig.CLASSES.values())}")
    print(f"📖 Total Subjects: 100+ subjects across all streams")
    print(f"🎓 Total Exams: {len(UniversalConfig.get_all_exams())} exams")
    print(f"🌍 Total Languages: {len(UniversalConfig.get_all_languages())} languages")
    
    print("\n📊 Coverage:")
    print(f"   • School Boards: {len(UniversalConfig.EXAMS['school_boards']['State Boards']) + 3}")
    print(f"   • Medical Exams: {len(UniversalConfig.EXAMS['medical'])}")
    print(f"   • Engineering Exams: {len(UniversalConfig.EXAMS['engineering'])}")
    print(f"   • Government Jobs: {len(UniversalConfig.EXAMS['government'])}")
    print(f"   • Professional: {len(UniversalConfig.EXAMS['professional'])}")
    print(f"   • International: {len(UniversalConfig.EXAMS['international'])}")
    
    print("\n🌐 Language Support:")
    print(f"   • Indian Languages: 22 (All constitutional languages)")
    print(f"   • International: 10 major languages")
    
    # Save to JSON
    config = UniversalConfig.export_config()
    with open('visionwire_universal_config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print("\n✅ Configuration exported to: visionwire_universal_config.json")
