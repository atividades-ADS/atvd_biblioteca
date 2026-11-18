from django.core.exceptions import ValidationError

def validate_file_size(file):
    limit_mb = 1
    if file.size > limit_mb * 1024 * 1024: # size está em bytes
        raise ValidationError(f"O arquivo deve ter no máximo {limit_mb} MB.")