import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BackdropService {
  private _visible$ = new BehaviorSubject<boolean>(false);
  public visible$ = this._visible$.asObservable(); // For components to subscribe to

  show(): void {
    this._visible$.next(true);
  }

  hide(): void {
      this._visible$.next(false);
  }

  toggle(): void {
    this._visible$.next(!this._visible$.value);
  }
}
