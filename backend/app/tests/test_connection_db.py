from app.database import get_supabase

def test_supabase_connection():
    supabase = get_supabase()

    try:
        response = supabase.table("consultas").select("*", count="exact").limit(1).execute()

        assert response.data is not None
        
    except Exception as e:
        raise e

if __name__ == "__main__":
    test_supabase_connection()