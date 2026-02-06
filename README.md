# VisionWire AI - Universal Configuration

Configuration module for the VisionWire AI system, covering the entire Indian Education System.

## Features

- **Comprehensive Coverage**: Classes 1-12, UG, PG.
- **Subjects**: 100+ subjects across Science, Commerce, and Arts streams.
- **Exams**: 50+ exams including JEE, NEET, UPSC, SSC, GATE.
- **Languages**: 22+ Indian and 10 International languages.
- **Difficulty Levels**: From easy to competitive exam level.

## Usage

```python
from visionwire_universal_config import UniversalConfig

# Get subjects for Class 12
subjects = UniversalConfig.get_subjects_for_class('12')
print(subjects)

# Export full config
config = UniversalConfig.export_config()
```

## Structure

The configuration is organized into:

- `CLASSES`: Education levels.
- `SUBJECTS`: Mapped by class/stream.
- `EXAMS`: Categorized by type (School, Medical, Engineering, etc.).
- `LANGUAGES`: Supported languages.
- `SYLLABUS_SOURCES`: Links and sources.
- `AGE_GROUPS`: Target audience profiles.
