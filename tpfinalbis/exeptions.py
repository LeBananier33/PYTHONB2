class ErreurBibliotheque(Exception):
    """Exception personnalisée pour les erreurs de la bibliothèque."""
    def __init__(self, message):
        super().__init__(message)
