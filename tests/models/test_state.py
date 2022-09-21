from src.app.models.state import State

def test_new_state():
  state = State.seed(
      1,
      "Texas",
      "TX"
  )

  assert state.country_id == 1
  assert state.name == 'Texas'
  assert state.initials == 'TX'
  

