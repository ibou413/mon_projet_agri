import 'package:flutter/material.dart';
import '../services/api_service.dart';

class HomeScreen extends StatelessWidget {
  final ApiService apiService = ApiService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('SUKELAGRI Home'),
      ),
      body: Center(
        child: FutureBuilder(
          future: apiService.get('welcome/'), // Exemple d'appel API
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return CircularProgressIndicator();
            } else if (snapshot.hasError) {
              return Text('Error: ${snapshot.error}');
            } else {
              return Text('Data: ${snapshot.data}');
            }
          },
        ),
      ),
    );
  }
}
