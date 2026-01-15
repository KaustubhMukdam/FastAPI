import inspect
from fastapi import Form

"""
This file contains the decorator that adds an 'as_form' class method to a Pydantic model allowing it to be instantiated from form data submitted via HTTP requests
"""

__all__ = ['as_form']

def as_form(cls):
    new_params = []
    for field_name, model_field in cls.model_fields.items():
        new_params.append(
            inspect.Parameter(
                field_name,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
                default=Form(...) if model_field.is_required() else Form(model_field.default),
                annotation=model_field.annotation,
            )
        )
    
    async def _as_form(**data):
        return cls(**data)
    
    sig = inspect.Signature(new_params)
    _as_form.__signature__ = sig
    setattr(cls, 'as_form', _as_form)
    return cls