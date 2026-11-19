from django.core.exceptions import ValidationError
import datetime


def validate_year(value):
    current_year = datetime.datetime.now().year
    if value < 1450 or value > current_year:
        raise ValidationError(f"O ano deve estar entre 1450 e {current_year}.")
    
def validate_min_length(value):
    if len(value) < 3:
        raise ValidationError("O título deve ter pelo menos 3 caracteres.")
    
def validate_number_of_pages(value):
    if value < 1:
        raise ValidationError("O número de páginas deve ser maior que zero.")
    if value > 5000:
        raise ValidationError("O número de páginas deve ser menor que 5000.")
    
def validate_isbn(value):
    if len(value) != 13:
        raise ValidationError("O ISBN deve ter exatamente 13 caracteres.")
    
def validate_size_of_file(value):
    tamanho_maximo = 20 * 1024 * 1024 
    if value.size > tamanho_maximo:
        raise ValidationError(f"O tamanho do arquivo não pode exceder {tamanho_maximo / (1024 * 1024)} MB.")
    
def FileExtensionValidator(value):
    extensoes_permitidas = ['.jpg', '.jpeg', '.png']
    if not any(value.name.lower().endswith(ext) for ext in extensoes_permitidas):
        raise ValidationError(f"Extensão de arquivo inválida. As extensões permitidas são: {', '.join(extensoes_permitidas)}.")