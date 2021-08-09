import React, { Component } from 'react';

class App extends Component {
  state = {
    food_item: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/item-list/'); // fetch data from django backend
      const food_item = await res.json();
      this.setState({
        food_item
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        <h1 class="title">General Store Listings</h1>
        <h4>Create, update or delete a listing from the <a href="http://localhost:8000/api/">backend</a> or
         the <a href="http://127.0.0.1:8000/admin/login/?next=/admin/">admin page</a></h4>
        <hr></hr>
        {this.state.food_item.map(item => (
          <div key={item.id}>
            <h3>{item.name}</h3>
            <span>{item.price}</span>
            <h6>Added: {item.created_at}</h6>
          </div>
        ))}
      </div>
    );
  }
}

export default App;